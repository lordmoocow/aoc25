"""Advent of Code 2025 - Day 01: Secret Entrance"""

def read_instructions(input_data) -> list[int]:
    lines = input_data.strip().split("\n")
    return [rotate(line) for line in lines]

def rotate(instruction: str) -> int:
    """Read instruction line"""
    i: int = int(instruction[1:])
    if instruction[0] == "R":
        return i
    else:
        return -i

def part1(input_data: str) -> int | str:
    """The Safe is a Decoy"""

    # Read each line and determine rotation direction R=+/L=-
    operations = read_instructions(input_data)

    # Track "0" count for result
    count: int = 0

    # Start at position 50
    selected: int = 50

    for op in operations:
        # Rotate in direction of operation (- goes backwards)
        selected += op

        # Mod 100 will wrap values values around 0-99
        selected %= 100

        # Check if we are at 0 exactly
        count += selected == 0

    return count

