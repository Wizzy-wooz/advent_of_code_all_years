from collections import deque
from math import lcm
from pathlib import Path
import re


def solve(d, rounds, relief):
    blocks = d.strip().split("\n\n");
    items = [];
    ops = [];
    div = [];
    yes = [];
    no = []
    for b in blocks:
        lines = b.splitlines();
        items.append(deque(map(int, re.findall(r"\d+", lines[1]))));
        ops.append(lines[2].split("= ")[1]);
        div.append(int(re.search(r"\d+", lines[3]).group()));
        yes.append(int(re.search(r"\d+", lines[4]).group()));
        no.append(int(re.search(r"\d+", lines[5]).group()))
    mod = lcm(*div);
    counts = [0] * len(items)
    for _ in range(rounds):
        for i in range(len(items)):
            while items[i]:
                old = items[i].popleft();
                value = eval(ops[i], {}, {"old": old});
                value = value // 3 if relief else value % mod;
                target = yes[i] if value % div[i] == 0 else no[i];
                items[target].append(value);
                counts[i] += 1
    a = sorted(counts);
    return a[-1] * a[-2]


def part1(d): return solve(d, 20, True)


def part2(d): return solve(d, 10000, False)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
