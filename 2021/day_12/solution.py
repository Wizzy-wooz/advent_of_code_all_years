from collections import defaultdict
from functools import lru_cache
from pathlib import Path


def solve(d, twice=False):
    g = defaultdict(list)
    for line in d.splitlines():
        if line.strip(): a, b = line.split("-");g[a].append(b);g[b].append(a)

    @lru_cache(None)
    def visit(node, seen, used):
        if node == "end": return 1
        total = 0
        for nxt in g[node]:
            if nxt == "start": continue
            if nxt.islower():
                if nxt not in seen:
                    total += visit(nxt, seen | {nxt}, used)
                elif twice and not used and nxt != "end":
                    total += visit(nxt, seen, True)
            else:
                total += visit(nxt, seen, used)
        return total

    return visit("start", frozenset({"start"}), not twice)


def part1(d): return solve(d)


def part2(d): return solve(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
