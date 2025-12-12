"""Advent of Code 2025 - Day 11."""

def load_devices(input_data: str) -> dict[str, set[str]]:
    return dict([(name, set(outputs.split()))
        for name, _ ,outputs in [line.partition(": ")
            for line in input_data.strip().splitlines()
        ]
    ])


def device_paths(devices: dict[str, set[str]], device: str, required: tuple[str, ...] | None = None, known: dict[tuple[str, tuple[str, ...] | None], int] = {}) -> int:
    if required and device in required:
        tmp = list(required)
        tmp.remove(device)
        required = tuple(tmp)
    
    if "out" in devices[device]:
        return 1 if not required else 0
    
    count = 0
    for output in devices[device]:
        if (output, required) in known:
            count += known[(output, required)]
        else:
            n = device_paths(devices, output, required, known)
            known[(output, required)] = n
            count += n
    return count


# def device_paths(devices: dict[str, set[str]], device: str) -> int:
#     if "out" in devices[device]:
#         return 1 
#     return sum(device_paths(devices, output) for output in devices[device])


def part1(input_data: str) -> int:
    devices = load_devices(input_data)
    return device_paths(devices, "you")


def part2(input_data: str) -> int:
    devices = load_devices(input_data)
    return device_paths(devices, "svr", ("dac", "fft"))

