from collections import defaultdict
from itertools import combinations
from pathlib import Path


def solve(d):
    g = d.splitlines();
    h = len(g);
    w = len(g[0]);
    freq = defaultdict(list)
    for y, r in enumerate(g):
        for x, c in enumerate(r):
            if c != ".": freq[c].append((x, y))
    p1 = set();
    p2 = set()
    for pts in freq.values():
        for (x, y), (a, b) in combinations(pts, 2):
            dx = a - x;
            dy = b - y
            for p in ((x - dx, y - dy), (a + dx, b + dy)):
                if 0 <= p[0] < w and 0 <= p[1] < h: p1.add(p)
            for sx, sy in ((x, y), (a, b)):
                t = 0
                while 0 <= sx - t * dx < w and 0 <= sy - t * dy < h: p2.add((sx - t * dx, sy - t * dy));t += 1
                t = 1
                while 0 <= sx + t * dx < w and 0 <= sy + t * dy < h: p2.add((sx + t * dx, sy + t * dy));t += 1
    return len(p1), len(p2)


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
