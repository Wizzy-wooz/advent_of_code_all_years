from pathlib import Path
import re


def rows(d): return [re.fullmatch(r"(\d+)-(\d+) (\w): (\w+)", x).groups() for x in d.splitlines() if x.strip()]


def part1(d): return sum(int(a) <= pw.count(c) <= int(b) for a, b, c, pw in rows(d))


def part2(d): return sum((pw[int(a) - 1] == c) ^ (pw[int(b) - 1] == c) for a, b, c, pw in rows(d))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
