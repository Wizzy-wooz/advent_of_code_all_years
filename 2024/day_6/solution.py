from pathlib import Path


def run(g, block=None):
    h = len(g);
    w = len(g[0]);
    x, y = next((x, y) for y, r in enumerate(g) for x, c in enumerate(r) if c in "^>v<");
    dirs = ((0, -1), (1, 0), (0, 1), (-1, 0));
    d = "^>v<".index(g[y][x]);
    seen = set();
    visited = set()
    while (x, y, d) not in seen:
        seen.add((x, y, d));
        visited.add((x, y));
        dx, dy = dirs[d];
        nx, ny = x + dx, y + dy
        if not (0 <= nx < w and 0 <= ny < h): return visited, False
        if g[ny][nx] == "#" or (nx, ny) == block:
            d = (d + 1) % 4
        else:
            x, y = nx, ny
    return visited, True


def solve(d):
    g = d.splitlines();
    visited, _ = run(g);
    return len(visited), sum(run(g, p)[1] for p in visited if g[p[1]][p[0]] == ".")


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
