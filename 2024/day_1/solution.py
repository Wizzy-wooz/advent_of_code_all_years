from collections import Counter
from pathlib import Path


def parse(d): return zip(*(map(int, l.split()) for l in d.splitlines() if l.strip()))


def solve(d):
    a, b = map(sorted, parse(d));
    return sum(abs(x - y) for x, y in zip(a, b)), sum(x * Counter(b)[x] for x in a)


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
