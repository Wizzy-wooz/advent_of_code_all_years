from pathlib import Path


def solve(d):
    a = list(map(int, d.strip().split(",")));
    lo = min(a);
    hi = max(a)
    return min(sum(abs(x - p) for x in a) for p in range(lo, hi + 1)), min(
        sum((n := abs(x - p)) * (n + 1) // 2 for x in a) for p in range(lo, hi + 1))


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
