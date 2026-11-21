from pathlib import Path


def parse(d):
    rocks = set()
    for line in d.splitlines():
        pts = [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
        for (x, y), (a, b) in zip(pts, pts[1:]):
            for xx in range(min(x, a), max(x, a) + 1):
                for yy in range(min(y, b), max(y, b) + 1): rocks.add((xx, yy))
    return rocks


def simulate(d, floor=False):
    rock = parse(d);
    bottom = max(y for x, y in rock);
    blocked = set(rock);
    count = 0;
    limit = bottom + 2
    while (500, 0) not in blocked:
        x, y = 500, 0
        while True:
            if not floor and y > bottom: return count
            for p in ((x, y + 1), (x - 1, y + 1), (x + 1, y + 1)):
                if (not floor or p[1] < limit) and p not in blocked: x, y = p;break
            else:
                blocked.add((x, y));count += 1;break
    return count


def part1(d): return simulate(d)


def part2(d): return simulate(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
