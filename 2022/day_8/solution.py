from pathlib import Path


def solve(d):
    g = [[int(c) for c in r.strip()] for r in d.splitlines() if r.strip()];
    h = len(g);
    w = len(g[0]);
    vis = 0;
    best = 0
    for y in range(h):
        for x in range(w):
            dirs = [[(xx, y) for xx in range(x - 1, -1, -1)], [(xx, y) for xx in range(x + 1, w)],
                    [(x, yy) for yy in range(y - 1, -1, -1)], [(x, yy) for yy in range(y + 1, h)]]
            vis += any(all(g[yy][xx] < g[y][x] for xx, yy in ray) for ray in dirs);
            score = 1
            for ray in dirs:
                n = 0
                for xx, yy in ray:
                    n += 1
                    if g[yy][xx] >= g[y][x]: break
                score *= n
            best = max(best, score)
    return vis, best


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
