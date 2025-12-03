"""Advent of Code 2025 - Day 02."""

def read_product_ids(input_data: str) -> list[tuple[int, int]]:
      return [
          (int(start), int(end))
          for start, end in (r.split('-') for r in input_data.split(','))
      ]

def validate(product_id: int) -> bool:
    pid = str(product_id)
    mid = len(pid) // 2
    return pid[:mid] != pid[mid:]

def part1(input_data: str) -> int:
    """Invalid Product IDs"""
    product_ranges = read_product_ids(input_data)

    count = 0
    for start, end in product_ranges:
        for i in range(start, end+1):
            if not validate(i):
                count += i
    return count
             


