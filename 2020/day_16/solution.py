from math import prod
from pathlib import Path
import re


def parse(d):
    rules_text, mine_text, near_text = d.split("\n\n");
    rules = {}
    for line in rules_text.splitlines():
        name, ranges = line.split(": ");
        rules[name] = [tuple(map(int, x)) for x in re.findall(r"(\d+)-(\d+)", ranges)]
    mine = list(map(int, mine_text.splitlines()[1].split(",")));
    near = [list(map(int, x.split(","))) for x in near_text.splitlines()[1:] if x]
    return rules, mine, near


def solve(d):
    rules, mine, tickets = parse(d);
    valid = lambda n: any(a <= n <= b for rs in rules.values() for a, b in rs)
    err = sum(n for t in tickets for n in t if not valid(n));
    tickets = [t for t in tickets if all(valid(n) for n in t)] + [mine]
    poss = {i: {name for name, rs in rules.items() if all(any(a <= t[i] <= b for a, b in rs) for t in tickets)} for i in
            range(len(mine))};
    mapping = {}
    while len(mapping) < len(mine):
        i = next(i for i, v in poss.items() if i not in mapping and len(v) == 1);
        name = next(iter(poss[i]));
        mapping[i] = name
        for j in poss:
            if j != i: poss[j].discard(name)
    return err, prod(mine[i] for i, n in mapping.items() if n.startswith("departure"))


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
