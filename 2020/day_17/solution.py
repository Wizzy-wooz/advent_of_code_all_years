from itertools import product
from pathlib import Path


def run(d, dim):
    active = {(x, y, *([0] * (dim - 2))) for y, row in enumerate(d.splitlines()) for x, c in enumerate(row) if
              c == "#"};
    offsets = [p for p in product((-1, 0, 1), repeat=dim) if any(p)]
    for _ in range(6):
        counts = {}
        for p in active:
            for off in offsets: q = tuple(a + b for a, b in zip(p, off));counts[q] = counts.get(q, 0) + 1
        active = {p for p, n in counts.items() if n == 3 or n == 2 and p in active}
    return len(active)


def part1(d): return run(d, 3)


def part2(d): return run(d, 4)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
