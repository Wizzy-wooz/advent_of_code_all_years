from itertools import cycle
from pathlib import Path


def changes(data: str) -> list[int]: return [int(line) for line in data.splitlines() if line.strip()]


def part1(data: str) -> int: return sum(changes(data))


def part2(data: str) -> int:
    seen, total = {0}, 0
    for value in cycle(changes(data)):
        total += value
        if total in seen: return total
        seen.add(total)
    raise AssertionError


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
