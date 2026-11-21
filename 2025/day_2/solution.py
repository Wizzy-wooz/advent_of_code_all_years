from pathlib import Path


def invalid(n, repeat):
    s = str(n)
    return any(len(s) % k == 0 and s == s[:len(s) // k] * k for k in range(2, repeat + 1))


def solve(data):
    a = b = 0
    for interval in data.strip().split(","):
        lo, hi = map(int, interval.split("-"))
        for n in range(lo, hi + 1):
            a += n if invalid(n, 2) else 0;
            b += n if invalid(n, len(str(n))) else 0
    return a, b


def part1(data): return solve(data)[0]


def part2(data): return solve(data)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
