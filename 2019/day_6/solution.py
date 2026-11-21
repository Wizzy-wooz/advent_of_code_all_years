from collections import defaultdict, deque
from pathlib import Path


def graph(data: str):
    parent = {};
    children = defaultdict(list)
    for line in data.splitlines():
        if line.strip(): a, b = line.strip().split(")");parent[b] = a;children[a].append(b)
    return parent, children


def part1(data: str) -> int:
    parent, _ = graph(data);
    return sum(_depth(n, parent) for n in parent)


def _depth(n, parent):
    d = 0
    while n in parent: n = parent[n];d += 1
    return d


def part2(data: str) -> int:
    parent, children = graph(data);
    start = parent["YOU"];
    goal = parent["SAN"];
    q = deque([(start, 0)]);
    seen = {start}
    while q:
        n, d = q.popleft()
        if n == goal: return d
        for m in children[n] + ([parent[n]] if n in parent else []):
            if m not in seen: seen.add(m);q.append((m, d + 1))
    raise ValueError("No orbital path between YOU and SAN")


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
