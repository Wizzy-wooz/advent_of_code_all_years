from pathlib import Path


def trees(d, dx, dy):
    g = d.splitlines();
    return sum(row[(i * dx) % len(row)] == "#" for i, row in enumerate(g[::dy]))


def part1(d): return trees(d, 3, 1)


def part2(d):
    from math import prod
    return prod(trees(d, x, y) for x, y in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
