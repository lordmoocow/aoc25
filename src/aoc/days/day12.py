"""Advent of Code 2025 - Day 12."""

import numpy as np

def load_presents(input_data: str) -> tuple[list[np.ndarray], list[tuple[np.ndarray, list[int]]]]:
    parts = input_data.split("\n\n")
    presents = [
        np.array([list(row) for row in shape[3:].splitlines()]) == "#"
        for shape in parts[:-1]
    ]
    trees = [
        (np.zeros((int(a), int(b)), bool), list(map(int, p.split())))
        for (a, _, b), p in [
            (dimensions.partition("x"), p)
            for dimensions, _, p in [
                tree.partition(": ")
                for tree in parts[-1].splitlines()
            ]
        ]
    ]
    return (presents, trees)


def flip_rotate(present: np.ndarray) -> list[np.ndarray]:
    orientations = []
    for flip in [present, np.fliplr(present)]:
        for r in range(4):
            rot = np.rot90(flip, r)
            if not any(np.array_equal(rot, o) for o in orientations):
                orientations.append(rot)
    return orientations


def placements(area: np.ndarray, present: np.ndarray):
    for x in range(np.size(area, 1) - present.shape[1] + 1):
        for y in range(np.size(area, 0) - present.shape[0] + 1):
            # check for overlaps
            placement = area[y:y+present.shape[0], x:x+present.shape[1]]
            if not (placement & present).any():
                # create a new area including the newly placed present
                a = area.copy()
                a[y:y+present.shape[0], x:x+present.shape[1]] |= present
                yield a  


def try_fit(area: np.ndarray, presents: list[np.ndarray]) -> bool:
    # if there are no remaining presents then we must have fit everything in
    if not presents:
        return True
    
    # if there isn't enough space remaining don't bother checking further
    required_area = sum(np.count_nonzero(p) for p in presents)
    remaining_space = np.size(area) - np.count_nonzero(area)
    if required_area > remaining_space:
        return False
    
    # take a present out of the pile to test with
    present = presents[0]
    # slice remaining presents (this copies so each branch will retain it's own list)
    remaining_presents = presents[1:]

    # in each orientation
    for orientation in flip_rotate(present):
        # each position
        for new_area in placements(area, orientation):
            # try remaining presents in remaining area
            # this will return true if all remaining presents fit so can exit as soon as we know
            if try_fit(new_area, remaining_presents):
                return True
    return False


def part1(input_data: str) -> int:
    presents, trees = load_presents(input_data)
    count = 0
    for area, pcount in trees:
        tofit = [
            presents[i]
            for i, n in enumerate(pcount)
            for _ in range(n)
            if n > 0
        ]
        
        if try_fit(area, tofit):
            print(f"{len(area)}x{len(area[0])}: fits")
            count += 1
        else:
            print(f"{len(area)}x{len(area[0])}: doesn't fit")

    return count

