"""Advent of Code 2025"""

import importlib
import time
from pathlib import Path
from typing import Annotated

import typer

from aoc.template import DAY_TEMPLATE

app = typer.Typer(help="Advent of Code 2025")

PROJECT_ROOT = Path(__file__).parent.parent.parent


@app.command()
def run(
    day: Annotated[int, typer.Argument(min=1, max=12, help="Day number (1-12)")],
    part: Annotated[int, typer.Option("-p", "--part", min=1, max=2, help="Part number (1 or 2)")],
    input_file: Annotated[str, typer.Option("-i", "--input", help="Input file name")] = "input.txt",
) -> None:
    """Run a day's solution."""
    # Import the day module
    module_name = f"aoc.days.day{day:02d}"
    try:
        day_module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        typer.echo(f"Day {day:02d} not found. Run 'aoc new {day}' to create it.", err=True)
        raise typer.Exit(1)

    # Read input file
    input_path = PROJECT_ROOT / "days" / f"{day:02d}" / input_file
    if not input_path.exists():
        typer.echo(f"Input file not found: {input_path}", err=True)
        raise typer.Exit(1)

    input_data = input_path.read_text()

    # Get the part function
    part_func = getattr(day_module, f"part{part}", None)
    if part_func is None:
        typer.echo(f"Part {part} not implemented for day {day:02d}", err=True)
        raise typer.Exit(1)

    # Run and time the solution
    start = time.perf_counter()
    result = part_func(input_data)
    elapsed = time.perf_counter() - start

    typer.echo(f"Day {day:02d} Part {part}: {result}")
    typer.echo(f"Time: {elapsed:.3f}s")


@app.command()
def new(
    day: Annotated[int, typer.Argument(min=1, max=25, help="Day number (1-25)")],
    force: Annotated[bool, typer.Option("--force", "-f", help="Overwrite existing files")] = False,
) -> None:
    """Scaffold a new day's solution."""
    # Create input directory
    input_dir = PROJECT_ROOT / "days" / f"{day:02d}"
    input_dir.mkdir(parents=True, exist_ok=True)

    # Create input files
    for filename in ["input.txt", "test.txt"]:
        filepath = input_dir / filename
        if not filepath.exists() or force:
            filepath.touch()
            typer.echo(f"Created {filepath.relative_to(PROJECT_ROOT)}")

    # Create solution file
    solution_path = PROJECT_ROOT / "src" / "aoc" / "days" / f"day{day:02d}.py"
    if solution_path.exists() and not force:
        typer.echo(f"Day {day:02d} already exists. Use --force to overwrite.", err=True)
        raise typer.Exit(1)

    solution_path.write_text(DAY_TEMPLATE.format(day=day))
    typer.echo(f"Created {solution_path.relative_to(PROJECT_ROOT)}")
    typer.echo(f"\nDay {day:02d} scaffolded successfully!")


if __name__ == "__main__":
    app()
