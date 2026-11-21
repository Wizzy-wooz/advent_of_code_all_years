from pathlib import Path


def marker(d, n):
    s = d.strip();
    return next(i + n for i in range(len(s) - n + 1) if len(set(s[i:i + n])) == n)


def part1(d): return marker(d, 4)


def part2(d): return marker(d, 14)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
