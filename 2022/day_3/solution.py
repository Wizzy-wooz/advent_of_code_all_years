from pathlib import Path


def priority(c): return ord(c) - 96 if c.islower() else ord(c) - 38


def part1(d): return sum(priority((set(s[:len(s) // 2]) & set(s[len(s) // 2:])).pop()) for s in d.splitlines() if s)


def part2(d):
    a = [s for s in d.splitlines() if s];
    return sum(priority((set(a[i]) & set(a[i + 1]) & set(a[i + 2])).pop()) for i in range(0, len(a), 3))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
