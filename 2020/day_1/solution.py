from itertools import combinations
from pathlib import Path


def solve(data):
    n = list(map(int, data.split()))
    return next(a * b for a, b in combinations(n, 2) if a + b == 2020), next(
        a * b * c for a, b, c in combinations(n, 3) if a + b + c == 2020)


def part1(data): return solve(data)[0]


def part2(data): return solve(data)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
