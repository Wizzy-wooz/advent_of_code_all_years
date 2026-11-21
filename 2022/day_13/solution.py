from functools import cmp_to_key
from pathlib import Path
import ast


def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int): return (a > b) - (a < b)
    if isinstance(a, int): a = [a]
    if isinstance(b, int): b = [b]
    for x, y in zip(a, b):
        c = cmp(x, y)
        if c: return c
    return (len(a) > len(b)) - (len(a) < len(b))


def part1(d):
    return sum(i for i, p in enumerate(d.strip().split("\n\n"), 1) if cmp(*map(ast.literal_eval, p.splitlines())) < 0)


def part2(d):
    a = [ast.literal_eval(x) for x in d.splitlines() if x.strip()];
    a.extend([[[2]], [[6]]]);
    a.sort(key=cmp_to_key(cmp));
    return (a.index([[2]]) + 1) * (a.index([[6]]) + 1)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
