from collections import Counter
from pathlib import Path
import re


def matches(line): a, b = line.split(":")[1].split("|");return len(
    set(map(int, re.findall(r"\d+", a))) & set(map(int, re.findall(r"\d+", b))))


def part1(d): return sum(2 ** (n - 1) for n in (matches(x) for x in d.splitlines() if x.strip()) if n)


def part2(d):
    a = [matches(x) for x in d.splitlines() if x.strip()];
    counts = [1] * len(a)
    for i, n in enumerate(a):
        for j in range(i + 1, min(len(a), i + n + 1)): counts[j] += counts[i]
    return sum(counts)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
