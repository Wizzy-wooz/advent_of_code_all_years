from collections import defaultdict
from math import atan2, gcd, pi
from pathlib import Path


def asteroids(data): return {(x, y) for y, row in enumerate(data.splitlines()) for x, c in enumerate(row) if c == "#"}


def directions(a, b):
    dx = b[0] - a[0];
    dy = b[1] - a[1];
    g = gcd(dx, dy);
    return dx // g, dy // g


def station(points): return max(points, key=lambda p: len({directions(p, q) for q in points if q != p}))


def part1(data):
    ps = asteroids(data);
    s = station(ps);
    return len({directions(s, p) for p in ps if p != s})


def part2(data):
    ps = asteroids(data);
    s = station(ps);
    groups = defaultdict(list)
    for p in ps:
        if p != s:
            d = directions(s, p);
            groups[d].append((abs(p[0] - s[0]) + abs(p[1] - s[1]), p))
    order = sorted(groups, key=lambda d: (atan2(d[0], -d[1]) + 2 * pi) % (2 * pi))
    vaporized = []
    while any(groups.values()):
        for d in order:
            if groups[d]: vaporized.append(min(groups[d])[1]);groups[d].remove(min(groups[d]))
    x, y = vaporized[199];
    return 100 * x + y


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
