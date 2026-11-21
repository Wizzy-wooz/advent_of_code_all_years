from pathlib import Path


def solve(d):
    a = list(map(int, d.split()));
    return sum(y > x for x, y in zip(a, a[1:])), sum(y > x for x, y in zip(a, a[3:]))


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
