"""Advent of Code 2025 - Day 04."""

def load_diagram(input_data: str) -> list[str]:
    return input_data.strip().splitlines()

def accessible(diagram: list[str], x, y: int) -> bool:
    count = 0
    for a in range(-1, 2):
        if x+a < 0 or x+a >= len(diagram):
            continue
        for b in range(-1, 2):
            if y+b < 0 or y+b >= len(diagram[0]):
                continue
            if not (a == b == 0) and diagram[x+a][y+b] == "@":
                count += 1
                
    return count < 4

def part1(input_data: str) -> int:
    """Accessible Forklifts"""
    diagram = load_diagram(input_data)
    return sum(
        1 
        for x,row in enumerate(diagram)
        for y,cell in enumerate(row)
        if cell == "@" and accessible(diagram, x, y)
    )

