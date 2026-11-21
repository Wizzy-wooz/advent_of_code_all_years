from heapq import heappop, heappush
from pathlib import Path


def shortest(d, times=1):
    g = [[int(c) for c in r.strip()] for r in d.splitlines() if r.strip()];
    h = len(g) * times;
    w = len(g[0]) * times;
    q = [(0, 0, 0)];
    best = {(0, 0): 0}
    while q:
        cost, x, y = heappop(q)
        if (x, y) == (w - 1, h - 1): return cost
        if cost != best[(x, y)]: continue
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h:
                r = (g[ny % len(g)][nx % len(g[0])] + nx // len(g[0]) + ny // len(g)) % 9 or 9;
                n = cost + r
                if n < best.get((nx, ny), 10 ** 20): best[(nx, ny)] = n;heappush(q, (n, nx, ny))


def part1(d): return shortest(d)


def part2(d): return shortest(d, 5)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
