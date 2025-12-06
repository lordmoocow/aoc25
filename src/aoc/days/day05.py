"""Advent of Code 2025 - Day 05."""

def load_stock(input_data: str) -> tuple[list[tuple[int, int]], set[int]]:
    sections = input_data.strip().split("\n\n")
    fresh = [(int(a), int(b)) for a, b in (r.split("-") for r in sections[0].splitlines())]
    available = set(map(int, sections[1].splitlines()))
    return (fresh, available)
    

def isfresh(fresh: list[tuple[int, int]], id: int) -> bool:
    for start, end in fresh:
        if id >= start and id <= end:
            return True
    return False


def part1(input_data: str) -> int:
    """Solve part 1."""
    fresh, ingredients = load_stock(input_data)
    return sum (
        1
        for ingredient in ingredients
        if isfresh(fresh, ingredient)
    )


def part2(input_data: str) -> int:
    fresh, _ = load_stock(input_data)
    fresh.sort()

    ranges = [fresh[0]]
    for start, end in fresh[1:]:
        min_start, max_end = ranges[-1]
        if start <= max_end:
            ranges[-1] = (min_start, max(max_end, end))
        else:
            ranges.append((start, end))

    return sum(
        end - start + 1 
        for start, end in ranges
    )
