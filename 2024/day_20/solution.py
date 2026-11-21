from collections import deque
from pathlib import Path


def solve(d, cheat=2, threshold=100):
    g = d.splitlines();
    h = len(g);
    w = len(g[0]);
    s = next((x, y) for y, r in enumerate(g) for x, c in enumerate(r) if c == "S");
    e = next((x, y) for y, r in enumerate(g) for x, c in enumerate(r) if c == "E")

    def bfs(start):
        q = deque([start]);
        dist = {start: 0}
        while q:
            x, y = q.popleft()
            for p in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= p[0] < w and 0 <= p[1] < h and g[p[1]][p[0]] != "#" and p not in dist: dist[p] = dist[(x,
                                                                                                               y)] + 1;q.append(
                    p)
        return dist

    a = bfs(s);
    z = bfs(e);
    base = a[e];
    count = 0
    for (x, y), d0 in a.items():
        for dx in range(-cheat, cheat + 1):
            for dy in range(-cheat, cheat + 1):
                t = abs(dx) + abs(dy);
                p = (x + dx, y + dy)
                if t <= cheat and p in z and base - (d0 + t + z[p]) >= threshold: count += 1
    return count


def part1(d): return solve(d, 2)


def part2(d): return solve(d, 20)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
