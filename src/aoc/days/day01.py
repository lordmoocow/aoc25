"""Advent of Code 2025 - Day 01: Secret Entrance"""

def read_instructions(input_data) -> list[int]:
    lines = input_data.strip().split("\n")
    return [rotate(line) for line in lines]

def rotate(instruction: str) -> int:
    i = int(instruction[1:])
    return i if instruction[0] == "R" else -i

def apply(selected: int, operation: int) -> int:
    # Rotate in direction of operation (- goes backwards)
    selected += operation
    # Mod 100 will wrap values around 0-99
    selected %= 100
    return selected

def part1(input_data: str) -> int:
    """The Password"""
    # Read each line and determine rotation direction R=+/L=-
    operations = read_instructions(input_data)
    # Track "0" count for result
    count = 0
    # Start at position 50
    selected = 50

    for op in operations:
        selected = apply(selected, op)
        count += selected == 0

    return count

def part2(input_data: str) -> int:
    """Password Method 0x434C49434B"""
    # Read each line and determine rotation direction R=+/L=-
    operations = read_instructions(input_data)
    # Track "0" count for result
    count = 0
    # Start at position 50
    selected = 50

    for op in operations:
        new_position = apply(selected, op)
        
        # Count full rotations
        count += abs(int(op / 100))
        # Ignore partial rotation if we _start_ on 0 as we would have already counted it
        if selected != 0:
            # Compare new dial position to the original position and direction of rotation
            if (op > 0 and new_position < selected) or (op < 0 and new_position > selected):
                count += 1
            # Or did we end on 0 exactly
            elif new_position == 0:
                count += 1

        selected = new_position

    return count
