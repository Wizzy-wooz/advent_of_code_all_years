from math import prod
from pathlib import Path


def wins(t, d):
    if (t // 2) * (t - t // 2) <= d: return 0
    lo, hi = 0, t // 2
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * (t - mid) > d:
            hi = mid
        else:
            lo = mid + 1
    return max(0, t - 2 * lo + 1)


def solve(d):
    a, b = d.splitlines();
    times = list(map(int, a.split()[1:]));
    dist = list(map(int, b.split()[1:]));
    return prod(wins(t, x) for t, x in zip(times, dist)), wins(int("".join(map(str, times))),
                                                               int("".join(map(str, dist))))


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
