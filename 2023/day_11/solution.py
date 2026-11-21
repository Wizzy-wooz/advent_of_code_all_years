from itertools import combinations
from pathlib import Path


def solve(d, factor):
    g = d.splitlines();
    h = len(g);
    w = len(g[0]);
    gal = [(x, y) for y, r in enumerate(g) for x, c in enumerate(r) if c == "#"];
    ex = [y for y in range(h) if all(g[y][x] == "." for x in range(w))];
    ey = [x for x in range(w) if all(g[y][x] == "." for y in range(h))]
    return sum(abs(x1 - x2) + abs(y1 - y2) + (factor - 1) * (
                sum(min(x1, x2) < x < xmax for x in ey) + sum(min(y1, y2) < y < ymax for y in ex)) for
               (x1, y1), (x2, y2) in combinations(gal, 2) for xmax, ymax in [(max(x1, x2), max(y1, y2))])


def part1(d): return solve(d, 2)


def part2(d): return solve(d, 1_000_000)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
