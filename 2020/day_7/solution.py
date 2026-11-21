from collections import defaultdict
from pathlib import Path
import re


def graph(d):
    g = defaultdict(list)
    for line in d.splitlines():
        if line.strip():
            outer, inside = line.split(" bags contain ")
            for n, color in re.findall(r"(\d+) ([a-z ]+) bag", inside): g[outer].append((int(n), color))
    return g


def part1(d):
    g = graph(d);
    rev = defaultdict(set)
    for a, items in g.items():
        for _, b in items: rev[b].add(a)
    found = set();
    todo = list(rev["shiny gold"])
    while todo:
        x = todo.pop()
        if x not in found: found.add(x);todo.extend(rev[x])
    return len(found)


def part2(d):
    g = graph(d)

    def count(x): return sum(n * (1 + count(y)) for n, y in g[x])

    return count("shiny gold")


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
