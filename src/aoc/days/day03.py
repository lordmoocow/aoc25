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
               


def joltage2(bank: str, cells: int) -> int:
    joltage = ""
    index = 0
    # repeate scan for the desired number of cells
    # always need to leave enough remaining cells so count down as we scan
    for x in range(cells-1, -1, -1):
        # scan for next highest number in remaining cells after last one
        # leave enough cells at the end to complete all
        j, i = scan(bank[index:len(bank)-x])
        # i is only relative to the sub str so add it to the full str index
        index += i + 1
        joltage += j
    return int(joltage)

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
