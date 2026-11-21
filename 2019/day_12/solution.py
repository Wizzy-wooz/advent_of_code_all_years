from itertools import combinations
from math import lcm
from pathlib import Path
import re


def parse(data): return [list(map(int, re.findall(r"-?\d+", line))) for line in data.splitlines() if line.strip()]


def axis_period(initial):
    pos = initial[:];
    vel = [0] * len(pos);
    t = 0
    while True:
        for i, j in combinations(range(len(pos)), 2):
            d = (pos[j] > pos[i]) - (pos[j] < pos[i]);
            vel[i] += d;
            vel[j] -= d
        pos = [p + v for p, v in zip(pos, vel)];
        t += 1
        if pos == initial and not any(vel): return t


def part1(data):
    p = parse(data);
    v = [[0] * 3 for _ in p]
    for _ in range(1000):
        for i, j in combinations(range(len(p)), 2):
            for k in range(3): d = (p[j][k] > p[i][k]) - (p[j][k] < p[i][k]);v[i][k] += d;v[j][k] -= d
        p = [[p[i][k] + v[i][k] for k in range(3)] for i in range(len(p))]
    return sum(sum(map(abs, a)) * sum(map(abs, b)) for a, b in zip(p, v))


def part2(data):
    p = parse(data);
    return lcm(*(axis_period([m[k] for m in p]) for k in range(3)))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
