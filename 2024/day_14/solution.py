from math import prod
from pathlib import Path
import re


def robots(d): return [tuple(map(int, re.findall(r"-?\d+", l))) for l in d.splitlines() if l.strip()]


def part1(d, w=101, h=103):
    q = [0] * 4
    for x, y, dx, dy in robots(d):
        x = (x + 100 * dx) % w;
        y = (y + 100 * dy) % h
        if x != w // 2 and y != h // 2: q[(y > h // 2) * 2 + (x > w // 2)] += 1
    return prod(q)


def part2(d, w=101, h=103):
    rs = robots(d);
    best = None;
    best_t = 0
    for t in range(w * h):
        ps = {((x + t * dx) % w, (y + t * dy) % h) for x, y, dx, dy in rs}
        # Compact clusters are a practical tree-pattern signal for the puzzle input.
        score = sum((x + 1, y) in ps for x, y in ps) + sum((x, y + 1) in ps for x, y in ps)
        if best is None or score > best: best = score;best_t = t
    return best_t


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
