from collections import deque
from pathlib import Path


def solve(d):
    g = [list(x) for x in d.splitlines()];
    h = len(g);
    w = len(g[0]);
    starts = []
    for y in range(h):
        for x in range(w):
            if g[y][x] == "S": start = (x, y);g[y][x] = "a"
            if g[y][x] == "E": end = (x, y);g[y][x] = "z"
    q = deque([(end, 0)]);
    dist = {end: 0}
    while q:
        (x, y), n = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and ord(g[ny][nx]) >= ord(g[y][x]) - 1 and (nx, ny) not in dist: dist[
                (nx, ny)] = n + 1;q.append(((nx, ny), n + 1))
    return dist[start], min(v for (x, y), v in dist.items() if g[y][x] == "a")


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
