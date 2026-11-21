from math import lcm
from pathlib import Path
import re


def parse(d): a, b = d.strip().split("\n\n");return a, {x: (y, z) for x, y, z in
                                                        re.findall(r"(\w+) = \((\w+), (\w+)\)", b)}


def part1(d):
    ins, g = parse(d);
    x = "AAA";
    i = 0
    while x != "ZZZ": x = g[x][0 if ins[i % len(ins)] == "L" else 1];i += 1
    return i


def part2(d):
    ins, g = parse(d);
    cycles = []
    for x in g:
        if x.endswith("A"):
            i = 0
            while not x.endswith("Z"): x = g[x][0 if ins[i % len(ins)] == "L" else 1];i += 1
            cycles.append(i)
    return lcm(*cycles)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
