from functools import lru_cache
from pathlib import Path


def solve(d):
    g = [[int(c) for c in r.strip()] for r in d.splitlines() if r.strip()];
    h = len(g);
    w = len(g[0])

    @lru_cache(None)
    def paths(x, y):
        if g[y][x] == 9: return {(x, y): 1}
        out = {}
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and g[ny][nx] == g[y][x] + 1:
                for p, n in paths(nx, ny).items(): out[p] = out.get(p, 0) + n
        return out

    scores = [paths(x, y) for y in range(h) for x in range(w) if g[y][x] == 0]
    return sum(len(s) for s in scores), sum(sum(s.values()) for s in scores)


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
