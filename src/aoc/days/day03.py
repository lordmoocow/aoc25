"""Advent of Code 2025 - Day 03."""


def load_battery_banks(input_data: str) -> list[str]:
    return input_data.strip().split("\n")


def scan(bank: str) -> tuple[str, int]:
    index, joltage = max(enumerate(bank), key=lambda x: int(x[1]))
    return joltage, index


def joltage(bank: str) -> int:
    j, i = scan(bank[:-1])
    j2, _ = scan(bank[i + 1:])
    return int(j + j2)


def joltage2(bank: str, cells: int) -> int:
    digits = []
    index = 0
    # repeat scan for the desired number of cells
    # always need to leave enough remaining cells so count down as we scan
    for x in range(cells-1, -1, -1):
        # scan for next highest number in remaining cells after last one
        # leave enough cells at the end to complete all
        j, i = scan(bank[index:len(bank)-x])
        # i is only relative to the sub str so add it to the full str index
        index += i + 1
        digits.append(j)
    return int("".join(digits))


def part1(input_data: str) -> int:
    """Maximum Joltage"""
    battery_banks = load_battery_banks(input_data)
    return sum(
        joltage(i) for i in battery_banks
    )


def part2(input_data: str) -> int:
    """Joltage Safety Override"""
    battery_banks = load_battery_banks(input_data)
    return sum(
        joltage2(i, 12) for i in battery_banks
    )
