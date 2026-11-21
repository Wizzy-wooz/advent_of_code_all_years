from math import lcm
from pathlib import Path
from collections import deque


def solve(d):
    g = d.splitlines();
    h = len(g) - 2;
    w = len(g[0]) - 2;
    start = (g[0].index("."), 0);
    end = (g[-1].index("."), h + 1);
    bl = []
    for y, row in enumerate(g[1:-1], 1):
        for x, c in enumerate(row[1:-1], 1):
            if c in "<>^v": bl.append((x, y, c))
    period = lcm(w, h);
    occ = []
    for t in range(period): occ.append({(((x - 1 + (t if c == ">" else -t if c == "<" else 0)) % w) + 1,
                                         ((y - 1 + (t if c == "v" else -t if c == "^" else 0)) % h) + 1) for x, y, c in
                                        bl})

    def trip(a, b, t0):
        q = deque([(a, t0)]);
        seen = {(a, t0 % period)}
        while q:
            (x, y), t = q.popleft()
            if (x, y) == b: return t
            for p in ((x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                nx, ny = p;
                nt = t + 1
                if p in (start, end) or 1 <= nx <= w and 1 <= ny <= h:
                    if p not in occ[nt % period] and (p, nt % period) not in seen: seen.add((p, nt % period));q.append(
                        (p, nt))
        raise ValueError("No route")

    t1 = trip(start, end, 0);
    t2 = trip(end, start, t1);
    return t1, trip(start, end, t2)


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
