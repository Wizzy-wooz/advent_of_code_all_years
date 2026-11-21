from pathlib import Path


def joltage(s, n):
    out = "";
    start = 0
    for left in range(n, 0, -1):
        i = max(range(start, len(s) - left + 1), key=lambda j: s[j]);
        out += s[i];
        start = i + 1
    return int(out)


def solve(d, n): return sum(joltage(line.strip(), n) for line in d.splitlines() if line.strip())


def part1(d): return solve(d, 2)


def part2(d): return solve(d, 12)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
