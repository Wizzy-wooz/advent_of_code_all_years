from pathlib import Path


def extrapolate(nums):
    rows = [nums]
    while any(rows[-1]): rows.append([b - a for a, b in zip(rows[-1], rows[-1][1:])])
    right = left = 0
    for row in reversed(rows): right = row[-1] + right;left = row[0] - left
    return left, right


def solve(d):
    vals = [extrapolate(list(map(int, x.split()))) for x in d.splitlines() if x.strip()];
    return sum(b for a, b in vals), sum(a for a, b in vals)


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
