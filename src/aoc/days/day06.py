"""Advent of Code 2025 - Day 06."""

def load_worksheet(input_data: str) -> tuple[list[list[int]], list[str]]:
    lines = input_data.strip().splitlines()

    numbers: list[list[int]] = []
    ops: list[str] = []

    for line in lines:
        line = line.strip().split()
        if not line[0].isdigit():
            ops = line
            break
        numbers.append([int(i) for i in line])

    return (numbers, ops)

def part1(input_data: str) -> int:
    """Cephalopod Worksheet"""
    numbers, ops = load_worksheet(input_data)
    answers = numbers[0]
    for row in numbers[1:]:
        for i, n in enumerate(row):
            if ops[i] == "+":
                answers[i] += n
            elif ops[i] == "*":
                answers[i] *= n

    return sum(answers)

