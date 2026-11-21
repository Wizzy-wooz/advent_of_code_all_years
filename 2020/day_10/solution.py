from collections import Counter
from pathlib import Path


def chain(d):
    a = sorted(map(int, d.split()));
    return [0] + a + [a[-1] + 3]


def part1(d):
    c = Counter(b - a for a, b in zip(chain(d), chain(d)[1:]));
    return c[1] * c[3]


def part2(d):
    a = chain(d);
    ways = {0: 1}
    for n in a[1:]: ways[n] = sum(ways.get(n - k, 0) for k in (1, 2, 3))
    return ways[a[-1]]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
