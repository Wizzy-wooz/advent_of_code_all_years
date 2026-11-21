from math import prod
from pathlib import Path


def parse(d):
    a, b = d.splitlines()[:2];
    return int(a), [(i, int(x)) for i, x in enumerate(b.split(",")) if x != "x"]


def part1(d):
    t, buses = parse(d);
    wait, bus = min(((n - t % n, n) for _, n in buses));
    return wait * bus


def part2(d):
    _, buses = parse(d);
    t = 0;
    step = 1
    for i, n in buses:
        while (t + i) % n: t += step
        step *= n
    return t


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
