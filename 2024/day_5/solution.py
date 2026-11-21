from pathlib import Path


def parse(d): a, b = d.strip().split("\n\n");rules = [tuple(map(int, x.split("|"))) for x in a.splitlines()];updates = [
    list(map(int, x.split(","))) for x in b.splitlines()];return rules, updates


def valid(u, r): return all(a not in u or b not in u or u.index(a) < u.index(b) for a, b in r)


def reorder(u, r):
    nodes = set(u);
    edges = {x: set() for x in u};
    ind = {x: 0 for x in u}
    for a, b in r:
        if a in nodes and b in nodes: edges[a].add(b)
    for a, bs in edges.items():
        for b in bs: ind[b] += 1
    out = []
    while len(out) < len(u):
        n = next(x for x in u if x not in out and ind[x] == 0);
        out.append(n);
        ind[n] = -1
        for b in edges[n]: ind[b] -= 1
    return out


def solve(d):
    r, us = parse(d);
    good = bad = 0
    for u in us:
        if valid(u, r):
            good += u[len(u) // 2]
        else:
            bad += reorder(u, r)[len(u) // 2]
    return good, bad


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
