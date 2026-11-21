from functools import lru_cache
from pathlib import Path


def solve(d):
    a, b = d.strip().split("\n\n");
    patterns = tuple(a.split(", "))

    @lru_cache(None)
    def ways(s):
        if not s: return 1
        return sum(ways(s[len(p):]) for p in patterns if s.startswith(p))

    vals = [ways(s) for s in b.splitlines()];
    return sum(x > 0 for x in vals), sum(vals)


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
