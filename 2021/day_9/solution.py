from math import prod
from pathlib import Path


def solve(d):
    g = [list(map(int, r.strip())) for r in d.splitlines() if r.strip()];
    h = len(g);
    w = len(g[0]);
    lows = [];
    basins = []
    for y in range(h):
        for x in range(w):
            ns = [g[ny][nx] for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) if
                  0 <= nx < w and 0 <= ny < h]
            if all(g[y][x] < n for n in ns): lows.append(g[y][x] + 1)
    seen = set()
    for y in range(h):
        for x in range(w):
            if g[y][x] == 9 or (x, y) in seen: continue
            stack = [(x, y)];
            seen.add((x, y));
            n = 0
            while stack:
                a, b = stack.pop();
                n += 1
                for p in ((a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)):
                    if 0 <= p[0] < w and 0 <= p[1] < h and g[p[1]][p[0]] < 9 and p not in seen: seen.add(
                        p);stack.append(p)
            basins.append(n)
    return sum(lows), prod(sorted(basins)[-3:])


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
