"""Advent of Code 2025 - Day 04."""


from itertools import product


def load_diagram(input_data: str) -> list[list[str]]:
    return [[x for x in line] for line in input_data.strip().splitlines()]


def accessible(diagram: list[list[str]], x: int, y: int) -> bool:
    height, width = len(diagram), len(diagram[0])
    count = sum(
        1
        for dx, dy in product(range(-1, 2), repeat=2)
        if (dx, dy) != (0, 0)
        and 0 <= x + dx < height
        and 0 <= y + dy < width
        and diagram[x + dx][y + dy] == "@"
    )
    return count < 4


def part1(input_data: str) -> int:
    """Accessible Forklifts"""
    diagram = load_diagram(input_data)
    return sum(
        1
        for x, row in enumerate(diagram)
        for y, cell in enumerate(row)
        if cell == "@" and accessible(diagram, x, y)
    )


def part2(input_data: str) -> int:
    """Shifting Paper"""
    diagram = load_diagram(input_data)
    removed = 0
    while removable := [
        (x, y)
        for x, row in enumerate(diagram)
        for y, cell in enumerate(row)
        if cell == "@" and accessible(diagram, x, y)
    ]:
        for roll_x, roll_y in removable:
            diagram[roll_x][roll_y] = "."
        removed += len(removable)
    return removed
