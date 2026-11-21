from math import prod
from pathlib import Path
import re


def parse(d):
    a, b = d.strip().split("\n\n");
    w = {}
    for line in a.splitlines():
        n, s = line.split("{");
        w[n] = s[:-1].split(",")
    parts = [dict((k, int(v)) for k, v in re.findall(r"([xmas])=(\d+)", x)) for x in b.splitlines()];
    return w, parts


def part1(d):
    w, parts = parse(d);
    total = 0
    for p in parts:
        node = "in"
        while node not in "AR":
            for rule in w[node]:
                if ":" not in rule: node = rule;break
                cond, dest = rule.split(":");
                m = re.fullmatch(r"([xmas])([<>])(\d+)", cond)
                if p[m[1]] < int(m[3]) if m[2] == "<" else p[m[1]] > int(m[3]): node = dest;break
        if node == "A": total += sum(p.values())
    return total


def part2(d):
    w, _ = parse(d)

    def count(node, ranges):
        if node == "R": return 0
        if node == "A": return prod(b - a + 1 for a, b in ranges.values())
        total = 0;
        remaining = ranges
        for rule in w[node]:
            if ":" not in rule: total += count(rule, remaining);break
            cond, dest = rule.split(":");
            key, op, n = cond[0], cond[1], int(cond[2:]);
            lo, hi = remaining[key]
            good = (lo, min(hi, n - 1)) if op == "<" else (max(lo, n + 1), hi);
            bad = (max(lo, n), hi) if op == "<" else (lo, min(hi, n))
            if good[0] <= good[1]: r = remaining.copy();r[key] = good;total += count(dest, r)
            if bad[0] > bad[1]: break
            remaining = remaining.copy();
            remaining[key] = bad
        return total

    return count("in", {c: (1, 4000) for c in "xmas"})


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
