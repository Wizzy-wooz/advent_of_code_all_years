from collections import deque
from pathlib import Path


def solve(d):
    cubes = {tuple(map(int, x.split(","))) for x in d.splitlines() if x.strip()};
    dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    area = sum(tuple(a + b for a, b in zip(c, v)) not in cubes for c in cubes for v in dirs)
    lo = [min(c[i] for c in cubes) - 1 for i in range(3)];
    hi = [max(c[i] for c in cubes) + 1 for i in range(3)];
    q = deque([tuple(lo)]);
    air = {tuple(lo)};
    outside = 0
    while q:
        c = q.popleft()
        for v in dirs:
            n = tuple(a + b for a, b in zip(c, v))
            if n in cubes:
                outside += 1
            elif all(lo[i] <= n[i] <= hi[i] for i in range(3)) and n not in air:
                air.add(n);q.append(n)
    return area, outside


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
