from pathlib import Path


def stabilize(d, visible=False):
    g = [list(x.strip()) for x in d.splitlines() if x.strip()];
    h = len(g);
    w = len(g[0]);
    dirs = [(dx, dy) for dy in (-1, 0, 1) for dx in (-1, 0, 1) if dx or dy]
    while True:
        n = [r.copy() for r in g];
        changed = False
        for y in range(h):
            for x in range(w):
                if g[y][x] == ".": continue
                count = 0
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    while 0 <= nx < w and 0 <= ny < h:
                        if g[ny][nx] != ".": count += g[ny][nx] == "#";break
                        if not visible: break
                        nx += dx;
                        ny += dy
                limit = 5 if visible else 4
                if g[y][x] == "L" and count == 0:
                    n[y][x] = "#";changed = True
                elif g[y][x] == "#" and count >= limit:
                    n[y][x] = "L";changed = True
        if not changed: return sum(r.count("#") for r in g)
        g = n


def part1(d): return stabilize(d)


def part2(d): return stabilize(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
