from math import prod
from pathlib import Path
import re


def solve(d):
    g = d.splitlines();
    nums = [];
    symbols = set();
    gears = {}
    for y, row in enumerate(g):
        for m in re.finditer(r"\d+", row): nums.append((int(m[0]), y, m.start(), m.end()))
        for x, c in enumerate(row):
            if c != "." and not c.isdigit(): symbols.add((x, y));
            if c == "*": gears[(x, y)] = []
    p1 = 0
    for n, y, a, b in nums:
        around = {(x, yy) for x in range(a - 1, b + 1) for yy in range(y - 1, y + 2)}
        if around & symbols: p1 += n
        for p in around & gears.keys(): gears[p].append(n)
    return p1, sum(prod(v) for v in gears.values() if len(v) == 2)


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
