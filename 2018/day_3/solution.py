from collections import Counter
from pathlib import Path
import re

PATTERN = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")


def claims(data: str):
    for line in data.splitlines():
        if line.strip():
            match = PATTERN.fullmatch(line.strip())
            if not match: raise ValueError(f"Invalid claim: {line}")
            yield tuple(map(int, match.groups()))


def analyze(data: str) -> tuple[int, int]:
    parsed = list(claims(data));
    fabric = Counter()
    for _, x, y, w, h in parsed:
        for xx in range(x, x + w):
            for yy in range(y, y + h): fabric[(xx, yy)] += 1
    overlap = sum(count > 1 for count in fabric.values())
    intact = next((claim_id for claim_id, x, y, w, h in parsed if
                   all(fabric[(xx, yy)] == 1 for xx in range(x, x + w) for yy in range(y, y + h))), None)
    if intact is None: raise ValueError("No non-overlapping claim found")
    return overlap, intact


def part1(data: str) -> int: return analyze(data)[0]


def part2(data: str) -> int: return analyze(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
