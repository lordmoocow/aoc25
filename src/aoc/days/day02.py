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

def validate2(product_id: int) -> bool:
    pid = str(product_id)
    pidlen = len(pid)
    mid = pidlen // 2
    # iterate through all possible substr lengths
    # after mid point it's impossible for substr to occur more than once
    for i in range(1, mid + 1):
        # how many times can substr fit in full str
        count, r = divmod(pidlen, i)
        # if the substr repeats exactly as many times as it can fit then it must be invalid
        if r == 0 and count == pid.count(pid[:i]):
            return False
    return True

def part1(input_data: str) -> int:
    """Invalid Product IDs"""
    product_ranges = read_product_ids(input_data)

    return sum(
        i for start, end in product_ranges
        for i in range(start, end + 1)
        if not validate(i)
    )
             
def part2(input_data: str) -> int:
    """More Invalid Product IDs"""
    product_ranges = read_product_ids(input_data)

    return sum(
        i for start, end in product_ranges
        for i in range(start, end + 1)
        if not validate2(i)
    )
