"""Advent of Code 2025 - Day 09."""

from typing import Iterable


def load_tiles(input_data: str) -> list[tuple[int, int]]:
    return [
        (int(x), int(y))
        for x, y in [
            tile.split(",")
            for tile in input_data.strip().splitlines()
        ]
    ]


class Rect:
    def __init__(self, a: tuple[int, int], b: tuple[int, int]) -> None:
        self.a = a
        self.b = b

    def width(self) -> int:
        return abs(self.b[0] - self.a[0]) + 1
    
    def height(self) -> int:
        return abs(self.b[1] - self.a[1]) + 1

    def area(self) -> int:
        return self.width() * self.height()


def find_rects(tiles: list[tuple[int, int]]):
    for a in tiles:
        for b in tiles:
            if a > b:
                yield Rect(a, b)


def find_largest_rect(rects: Iterable[Rect]) -> Rect:
    return max(rects, key=lambda x: x.area())


def part1(input_data: str) -> int:
    tiles = load_tiles(input_data)
    rects = find_rects(tiles)
    r = find_largest_rect(rects)
    return r.area()

