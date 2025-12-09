"""Advent of Code 2025 - Day 08."""


from math import prod


class JunctionBox:
    def __init__(self, index: int, pos: Vec3) -> None:
        self.index = index
        self.pos = pos

    def __repr__(self) -> str:
        return f"{self.pos}"


class Vec3:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"[{self.x},{self.y},{self.z}]"

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def sub(self, other: Vec3) -> Vec3:
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def mul(self, other: Vec3) -> Vec3:
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)

    def magsqr(self) -> int:
        return abs(sum(self.mul(self)))


def load_junction_box_coordinates(input_data: str) -> list[JunctionBox]:
    return [
        JunctionBox(i, Vec3(int(x), int(y), int(z)))
        for i, (x, y, z) in enumerate([
            xyz.split(",") for xyz in input_data.strip().splitlines()
        ])
    ]


def connect_junction_boxes(jboxes: list[JunctionBox]) -> list[tuple[int, int, int]]:
    boxes = [(i, j.pos) for i, j in enumerate(jboxes)]
    pairs = []
    # frmo each box (a), find distance to each other box (b)
    for i, a in boxes:
        for j, b in boxes:
            if j != i:
                d = a.sub(b).magsqr()
                pairs.append((i, j, d))

    # return  collection of pairs including their distance (sorted)
    return sorted(pairs, key=lambda x: x[2])


def trace_circuits(connections: list[tuple[int, int, int]]) -> tuple[list[set[int]], tuple[int, int]]:
    circuits: list[set[int]] = []
    last: tuple[int, int]=(0,0)

    def find(a: int) -> int | None:
        for i, c in enumerate(circuits):
            if a in c:
                return i

    for a, b, _ in connections:
        # find if either belongs to an existing circuit
        circuit_a = find(a)
        circuit_b = find(b)

        # if not, we will create a new one
        if circuit_a is None and circuit_b is None:
            circuits.append({a, b})
            last = (a, b)
        # if a was not found, connect it to b's circuit
        elif circuit_a is None and circuit_b is not None:
            circuits[circuit_b].add(a)
            last = (a, b)
        # if b was not found, connect it to a's circuit
        elif circuit_b is None and circuit_a is not None:
            circuits[circuit_a].add(b)
            last = (a, b)
        # if both were found, and are not in the same circuit, connect the two circuits
        elif circuit_a is not None and circuit_b is not None and circuit_a != circuit_b:
            circuits[circuit_b].update(circuits[circuit_a])
            circuits.remove(circuits[circuit_a])
            last = (a, b)

    return (circuits, last)



def part1(input_data: str) -> int:
    jboxes = load_junction_box_coordinates(input_data)
    connections = connect_junction_boxes(jboxes)[:2000]
    circuits, _ = trace_circuits(connections)
    return prod(map(len, sorted(circuits, key=len, reverse=True)[:3]))


def part2(input_data: str) -> int:
    jboxes = load_junction_box_coordinates(input_data)
    connections = connect_junction_boxes(jboxes)
    _, (a, b) = trace_circuits(connections)
    return jboxes[a].pos.x * jboxes[b].pos.x
