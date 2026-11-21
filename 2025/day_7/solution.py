from functools import lru_cache
from pathlib import Path


def solve(d):
    g = d.splitlines();
    start = next((x, y) for y, r in enumerate(g) for x, c in enumerate(r) if c == "S");
    splits = set();
    h = len(g);
    w = len(g[0])
    beams = {start[0]};
    for y in range(start[1] + 1, h):
        nxt = set()
        for x in beams:
            if g[y][x] == "^":
                splits.add((x, y));nxt.update((x - 1, x + 1))
            else:
                nxt.add(x)
        beams = {x for x in nxt if 0 <= x < w}

    @lru_cache(None)
    def timelines(x, y):
        if y >= h: return 1
        if g[y][x] == "^": return (timelines(x - 1, y + 1) if x else 0) + (timelines(x + 1, y + 1) if x + 1 < w else 0)
        return timelines(x, y + 1)

    return len(splits), timelines(start[0], start[1] + 1)


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
