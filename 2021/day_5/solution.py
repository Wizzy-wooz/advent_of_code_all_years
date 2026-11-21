from collections import Counter
from math import gcd
from pathlib import Path
import re


def solve(d):
    allpts = [];
    straight = []
    for line in d.splitlines():
        if not line.strip(): continue
        x1, y1, x2, y2 = map(int, re.findall(r"\d+", line));
        dx = x2 - x1;
        dy = y2 - y1;
        g = gcd(abs(dx), abs(dy));
        pts = [(x1 + i * dx // g, y1 + i * dy // g) for i in range(g + 1)];
        allpts += pts
        if dx == 0 or dy == 0: straight += pts
    return sum(n > 1 for n in Counter(straight).values()), sum(n > 1 for n in Counter(allpts).values())


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
