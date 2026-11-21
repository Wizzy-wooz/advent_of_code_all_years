from pathlib import Path


def energized(g, start):
    h = len(g);
    w = len(g[0]);
    stack = [start];
    seen = set();
    cells = set()
    while stack:
        x, y, dx, dy = stack.pop()
        if not (0 <= x < w and 0 <= y < h) or (x, y, dx, dy) in seen: continue
        seen.add((x, y, dx, dy));
        cells.add((x, y));
        c = g[y][x]
        if c == "/":
            dirs = [(-dy, -dx)]
        elif c == "\\":
            dirs = [(dy, dx)]
        elif c == "-" and dy:
            dirs = [(-1, 0), (1, 0)]
        elif c == "|" and dx:
            dirs = [(0, -1), (0, 1)]
        else:
            dirs = [(dx, dy)]
        stack.extend((x + a, y + b, a, b) for a, b in dirs)
    return len(cells)


def solve(d):
    g = d.splitlines();
    h = len(g);
    w = len(g[0]);
    return energized(g, (0, 0, 1, 0)), max(
        [energized(g, (x, 0, 0, 1)) for x in range(w)] + [energized(g, (x, h - 1, 0, -1)) for x in range(w)] + [
            energized(g, (0, y, 1, 0)) for y in range(h)] + [energized(g, (w - 1, y, -1, 0)) for y in range(h)])


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
