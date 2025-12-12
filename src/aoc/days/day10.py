"""Advent of Code 2025 - Day 10."""

import heapq

class Machine:
    def __init__(self, lights: list[bool], buttons: list[list[int]], joltage: list[int]) -> None:
        self.on_state = tuple(lights)
        self.buttons = buttons
        self.joltage = joltage

    def __repr__(self) -> str:
        return f"[{"".join(["#" if x else "." for x in self.on_state])}]"

    def activate(self) -> int:
        initial = tuple([False] * len(self.on_state))
        
        # (state, press_count)
        queue = [(0, initial)]
        # heapq sorts so that lower presses are prioritised
        heapq.heapify(queue)

        # track which states we have already tried
        tried = {initial}

        while queue:
            presses, state = heapq.heappop(queue)

            # starting from this state now try each button
            for button in self.buttons:
                # Apply button to get new state
                new_state = list(state)
                for b in button:
                    new_state[b] = not new_state[b]
                new_state = tuple(new_state)

                # if the last button activated then return now
                if new_state == self.on_state:
                    return presses + 1

                # it didn't activate, and we haven't yet tried the new state
                # queue it for exploration and track presses to get there
                if new_state not in tried:
                    tried.add(new_state)
                    heapq.heappush(queue, (presses + 1, new_state))

        return 0  # No solution found


def load_machines(input_data: str) -> list[Machine]:
    machines = []
    for line in input_data.strip().splitlines():
        parts = line.split()
        lights = [x == "#" for x in parts[0][1:-1]]
        buttons = [[int(x) for x in buttons[1:-1].split(",")] for buttons in parts[1:-1]]
        joltage = [int(x) for x in parts[-1][1:-1].split(",")]
        machines.append(Machine(lights, buttons, joltage))
    return machines


def part1(input_data: str) -> int:
    machines = load_machines(input_data)
    return sum(machine.activate() for machine in machines)

