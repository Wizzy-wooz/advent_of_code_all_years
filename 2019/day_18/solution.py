from collections import deque
from pathlib import Path


def solve(data, split=False):
    g = [list(r) for r in data.splitlines()];
    starts = [(x, y) for y, r in enumerate(g) for x, c in enumerate(r) if c == "@"]
    if split:
        x, y = starts[0]
        for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)): g[y + dy][x + dx] = "#"
        starts = [(x + dx, y + dy) for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1))]
        for x, y in starts: g[y][x] = "@"
    keys = sum(1 for r in g for c in r if c.islower());
    goal = (1 << keys) - 1
    q = deque([(tuple(starts), 0, 0)]);
    seen = {(tuple(starts), 0)};
    dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
    while q:
        pos, mask, dist = q.popleft()
        if mask == goal: return dist
        for i, (x, y) in enumerate(pos):
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy;
                c = g[ny][nx]
                if c == "#" or (c.isupper() and not mask & (1 << (ord(c.lower()) - 97))): continue
                newmask = mask | (1 << (ord(c) - 97)) if c.islower() else mask
                np = list(pos);
                np[i] = (nx, ny);
                state = (tuple(np), newmask)
                if state not in seen: seen.add(state);q.append((state[0], newmask, dist + 1))
    raise ValueError("Not all keys are reachable")


def part1(data): return solve(data)


def part2(data): return solve(data, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
