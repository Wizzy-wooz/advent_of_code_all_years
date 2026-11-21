from math import prod
from pathlib import Path


def problems(d, cephalopod=False):
    rows = d.splitlines();
    width = max(map(len, rows));
    rows = [r.ljust(width) for r in rows];
    groups = [];
    start = 0
    for x in range(width + 1):
        if x == width or all(r[x] == " " for r in rows):
            if start < x: groups.append((start, x))
            start = x + 1
    out = []
    for a, b in groups:
        op = rows[-1][a:b].strip();
        nums = []
        if cephalopod:
            for x in range(b - 1, a - 1, -1):
                n = "".join(r[x] for r in rows[:-1] if r[x].isdigit());
                if n: nums.append(int(n))
        else:
            nums = [int(n) for row in rows[:-1] for n in [row[a:b].strip()] if n]
        out.append(sum(nums) if op == "+" else prod(nums))
    return sum(out)


def part1(d): return problems(d)


def part2(d): return problems(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
