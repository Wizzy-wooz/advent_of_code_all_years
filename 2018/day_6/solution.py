from collections import Counter
from pathlib import Path


def points(data: str) -> list[tuple[int, int]]: return [tuple(map(int, line.split(", "))) for line in data.splitlines()
                                                        if line.strip()]


def areas(data: str, threshold: int = 10_000) -> tuple[int, int]:
    coords = points(data)
    minx, maxx = min(x for x, _ in coords), max(x for x, _ in coords)
    miny, maxy = min(y for _, y in coords), max(y for _, y in coords)
    counts = Counter();
    infinite = set();
    safe = 0
    for x in range(minx - threshold // max(1, len(coords)) - 1, maxx + threshold // max(1, len(coords)) + 2):
        for y in range(miny - threshold // max(1, len(coords)) - 1, maxy + threshold // max(1, len(coords)) + 2):
            distances = [abs(x - px) + abs(y - py) for px, py in coords]
            nearest = min(distances)
            if distances.count(nearest) == 1:
                owner = distances.index(nearest);
                counts[owner] += 1
                if x < minx or x > maxx or y < miny or y > maxy: infinite.add(owner)
            if sum(distances) < threshold: safe += 1
    return max((area for owner, area in counts.items() if owner not in infinite), default=0), safe


def part1(data: str) -> int: return areas(data)[0]


def part2(data: str, threshold: int = 10_000) -> int: return areas(data, threshold)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
