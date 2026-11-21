from heapq import heappop, heappush
from pathlib import Path


def solve(d):
    g = d.splitlines();
    h = len(g);
    w = len(g[0]);
    s = next((x, y) for y, r in enumerate(g) for x, c in enumerate(r) if c == "S");
    e = next((x, y) for y, r in enumerate(g) for x, c in enumerate(r) if c == "E");
    start = (*s, 0);
    q = [(0, *start)];
    dist = {start: 0};
    prev = {}
    while q:
        cost, x, y, di = heappop(q);
        state = (x, y, di)
        if cost != dist[state]: continue
        for nstate, wgt in (((x, y, (di + 1) % 4), 1000), ((x, y, (di - 1) % 4), 1000),
                            ((x + (1, 0, -1, 0)[di], y + (0, 1, 0, -1)[di], di), 1)):
            nx, ny, _ = nstate
            if g[ny][nx] == "#": continue
            nd = cost + wgt
            if nd < dist.get(nstate, 10 ** 20):
                dist[nstate] = nd;prev[nstate] = {state};heappush(q, (nd, *nstate))
            elif nd == dist.get(nstate):
                prev[nstate].add(state)
    ends = [(*e, i) for i in range(4) if (*e, i) in dist];
    best = min(dist[s] for s in ends);
    stack = [s for s in ends if dist[s] == best];
    states = set(stack)
    while stack:
        st = stack.pop()
        for p in prev.get(st, []):
            if p not in states: states.add(p);stack.append(p)
    return best, len({(x, y) for x, y, _ in states})


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
