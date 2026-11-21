from collections import deque
from pathlib import Path


def shortest(coords, n, limit):
    blocked = set(coords[:limit]);
    q = deque([((0, 0), 0)]);
    seen = {(0, 0)}
    while q:
        (x, y), d = q.popleft()
        if (x, y) == (n, n): return d
        for p in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= p[0] <= n and 0 <= p[1] <= n and p not in blocked and p not in seen: seen.add(p);q.append(
                (p, d + 1))
    return None


def solve(d, n=70, initial=1024):
    c = [tuple(map(int, l.split(","))) for l in d.splitlines() if l.strip()];
    p1 = shortest(c, n, initial);
    lo = initial;
    hi = len(c)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if shortest(c, n, mid) is None:
            hi = mid
        else:
            lo = mid
    return p1, ",".join(map(str, c[hi - 1]))


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
