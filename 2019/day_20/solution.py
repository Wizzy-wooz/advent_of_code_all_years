from collections import deque, defaultdict
from pathlib import Path


def parse(data):
    g = data.splitlines();
    h = len(g);
    w = max(map(len, g));
    g = [r.ljust(w) for r in g];
    portals = defaultdict(list)
    for y in range(h):
        for x in range(w):
            if not g[y][x].isupper(): continue
            for dx, dy in ((1, 0), (0, 1)):
                xx, yy = x + dx, y + dy
                if xx < w and yy < h and g[yy][xx].isupper():
                    name = g[y][x] + g[yy][xx]
                    ax, ay = (x - dx, y - dy) if 0 <= x - dx < w and 0 <= y - dy < h and g[y - dy][x - dx] == "." else (
                        xx + dx, yy + dy)
                    if 0 <= ax < w and 0 <= ay < h and g[ay][ax] == ".": portals[name].append((ax, ay))
    return g, portals


def shortest(data, recursive=False):
    g, ps = parse(data);
    start = ps["AA"][0];
    end = ps["ZZ"][0];
    h = len(g);
    w = len(g[0]);
    outer = set()
    for pts in ps.values():
        for x, y in pts:
            if x <= 2 or y <= 2 or x >= w - 3 or y >= h - 3: outer.add((x, y))
    mate = {p: q for pts in ps.values() for p, q in ([pts] if len(pts) == 2 else [])}
    q = deque([(start, 0, 0)]);
    seen = {(start, 0)}
    while q:
        (x, y), level, d = q.popleft()
        if (x, y) == end and level == 0: return d
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and g[ny][nx] == ".":
                state = ((nx, ny), level)
                if state not in seen: seen.add(state);q.append(((nx, ny), level, d + 1))
        if (x, y) in mate:
            nl = level + (-1 if (x, y) in outer else 1) if recursive else 0
            if nl >= 0:
                state = (mate[(x, y)], nl)
                if state not in seen: seen.add(state);q.append((mate[(x, y)], nl, d + 1))
    raise ValueError("No route through portal maze")


def part1(data): return shortest(data)


def part2(data): return shortest(data, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
