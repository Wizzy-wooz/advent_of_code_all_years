from itertools import combinations
from pathlib import Path


def graph(d):
    g = {}
    for line in d.splitlines():
        if line.strip(): a, b = line.split("-");g.setdefault(a, set()).add(b);g.setdefault(b, set()).add(a)
    return g


def part1(d):
    g = graph(d);
    return sum(any(n.startswith("t") for n in tri) for a in g for b in g[a] for c in g[a] & g[b] if a < b < c for tri in
               [(a, b, c)])


def part2(d):
    g = graph(d);
    best = set()

    def expand(clique, candidates):
        nonlocal best
        if len(clique) + len(candidates) <= len(best): return
        if not candidates:
            if len(clique) > len(best): best = clique
            return
        while candidates:
            v = candidates.pop();
            expand(clique | {v}, candidates & g[v])
            if len(clique) + len(candidates) <= len(best): break

    expand(set(), set(g));
    return ",".join(sorted(best))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
