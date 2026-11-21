from pathlib import Path
import re


def solve(d, bulk):
    a, b = d.split("\n\n");
    rows = a.splitlines();
    n = int(rows[-1].split()[-1]);
    stacks = [[] for _ in range(n)]
    for row in rows[:-1]:
        for i in range(n):
            c = row[1 + 4 * i] if 1 + 4 * i < len(row) else " "
            if c.isalpha(): stacks[i].insert(0, c)
    for count, src, dst in map(lambda x: map(int, x), re.findall(r"move (\d+) from (\d+) to (\d+)", b)):
        moving = stacks[src - 1][-count:];
        del stacks[src - 1][-count:]
        stacks[dst - 1].extend(moving if bulk else moving[::-1])
    return "".join(s[-1] for s in stacks)


def part1(d): return solve(d, False)


def part2(d): return solve(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
