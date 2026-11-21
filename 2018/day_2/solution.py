from collections import Counter
from itertools import combinations
from pathlib import Path


def ids(data: str) -> list[str]: return [line.strip() for line in data.splitlines() if line.strip()]


def part1(data: str) -> int:
    twos = threes = 0
    for box_id in ids(data):
        counts = Counter(box_id).values()
        twos += 2 in counts;
        threes += 3 in counts
    return twos * threes


def part2(data: str) -> str:
    for first, second in combinations(ids(data), 2):
        differences = [i for i, (a, b) in enumerate(zip(first, second)) if a != b]
        if len(first) == len(second) and len(differences) == 1:
            i = differences[0]
            return first[:i] + first[i + 1:]
    raise ValueError("No pair of box IDs differs by exactly one character")


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
