from collections import Counter
from pathlib import Path
import re

DELTAS = {"e": (1, 0), "w": (-1, 0), "ne": (1, -1), "nw": (0, -1), "se": (0, 1), "sw": (-1, 1)}


def initial(d):
    black = set()
    for line in d.splitlines():
        x = y = 0
        for step in re.findall(r"e|se|sw|w|nw|ne", line): dx, dy = DELTAS[step];x += dx;y += dy
        p = (x, y);
        black.symmetric_difference_update({p})
    return black


def part1(d): return len(initial(d))


def part2(d):
    b = initial(d)
    for _ in range(100):
        c = Counter((x + dx, y + dy) for x, y in b for dx, dy in DELTAS.values());
        b = {p for p, n in c.items() if n == 2 or n == 1 and p in b}
    return len(b)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
