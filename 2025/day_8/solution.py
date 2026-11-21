from itertools import combinations
from math import prod
from pathlib import Path


def solve(d):
    pts = [tuple(map(int, l.split(","))) for l in d.splitlines() if l.strip()];
    edges = sorted(
        (sum((a[k] - b[k]) ** 2 for k in range(3)), i, j) for i, j in combinations(range(len(pts)), 2) for a, b in
        [(pts[i], pts[j])]);
    parent = list(range(len(pts)));
    size = [1] * len(pts)

    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]];x = parent[x]
        return x

    k = 10 if len(pts) <= 20 else 1000
    for _, i, j in edges[:k]:
        a, b = find(i), find(j)
        if a != b: parent[a] = b;size[b] += size[a]
    p1 = prod(sorted((size[i] for i in range(len(pts)) if find(i) == i), reverse=True)[:3]);
    p2 = None
    for _, i, j in edges:
        a, b = find(i), find(j)
        if a != b:
            parent[a] = b;
            size[b] += size[a]
            if size[b] == len(pts): p2 = pts[i][0] * pts[j][0];break
    return p1, p2


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
