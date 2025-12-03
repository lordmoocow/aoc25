"""Advent of Code 2025 - Day 03."""


def load_battery_banks(input_data: str) -> list[str]:
    lines = input_data.strip().split("\n")
    return [line for line in lines]


def scan(bank: str) -> tuple[str, int]:
    index, joltage = 0, 0
    for i, cell in enumerate(bank):
        cell = int(cell)

        # does this sell have a higher joltage?
        # track which index it was at for next scan
        if cell > joltage:
            joltage = cell
            index = i

    # return cell joltage and it's bank index
    return (str(joltage), index)


def joltage(bank: str) -> int:
    j, i = scan(bank[:-1])
    j2, _ = scan(bank[i + 1:])
    return int(j + j2)
               

def part1(input_data: str) -> int:
    """Maximum Joltage"""
    battery_banks = load_battery_banks(input_data)
    return sum(
        joltage(i) for i in battery_banks
    )
