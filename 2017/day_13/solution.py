from math import prod
from pathlib import Path


def parse(data: str) -> dict[int, int]:
    return {int(depth): int(rng) for line in data.splitlines() if line.strip() for depth, rng in [line.split(": ")]}


def part1(data: str) -> int:
    layers = parse(data)
    return sum(depth * rng for depth, rng in layers.items() if rng == 1 or depth % (2 * (rng - 1)) == 0)


def part2(data: str) -> int:
    layers = parse(data)
    if any(rng == 1 for rng in layers.values()):
        raise ValueError("A range-one scanner makes safe passage impossible")
    delay = 0
    while any((depth + delay) % (2 * (rng - 1)) == 0 for depth, rng in layers.items()):
        delay += 1
    return delay


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
