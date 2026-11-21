from pathlib import Path
import re


def solve(d, offset=0):
    total = 0
    for block in d.strip().split("\n\n"):
        a, b, p = [tuple(map(int, re.findall(r"\d+", line))) for line in block.splitlines()];
        px, py = p[0] + offset, p[1] + offset;
        det = a[0] * b[1] - a[1] * b[0]
        if det:
            na = px * b[1] - py * b[0];
            nb = a[0] * py - a[1] * px
            if na % det == nb % det == 0: total += 3 * (na // det) + nb // det
    return total


def part1(d): return solve(d)


def part2(d): return solve(d, 10_000_000_000_000)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
