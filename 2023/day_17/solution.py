from heapq import heappop, heappush
from pathlib import Path


def least(d, minrun, maxrun):
    g = [[int(c) for c in r] for r in d.splitlines()];
    h = len(g);
    w = len(g[0]);
    q = [(0, 0, 0, -1, 0)];
    best = {}
    while q:
        cost, x, y, dirn, run = heappop(q)
        if (x, y) == (w - 1, h - 1) and run >= minrun: return cost
        if (x, y, dirn, run) in best and best[x, y, dirn, run] < cost: continue
        for nd, (dx, dy) in enumerate(((1, 0), (0, 1), (-1, 0), (0, -1))):
            if dirn >= 0 and nd == (dirn + 2) % 4: continue
            nr = run + 1 if nd == dirn else 1
            if nd != dirn and dirn >= 0 and run < minrun or nr > maxrun: continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                nc = cost + g[ny][nx];
                key = (nx, ny, nd, nr)
                if nc < best.get(key, 10 ** 30): best[key] = nc;heappush(q, (nc, nx, ny, nd, nr))
    raise ValueError("No valid route")


def part1(d): return least(d, 1, 3)


def part2(d): return least(d, 4, 10)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
