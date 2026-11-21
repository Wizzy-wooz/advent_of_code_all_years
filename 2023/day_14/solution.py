from pathlib import Path


def tilt(g, d):
    h = len(g);
    w = len(g[0]);
    g = [list(r) for r in g]
    lines = range(w) if d in "NS" else range(h)
    for line in lines:
        coords = [[(x, line) for x in range(h)] if d == "W" else [(w - 1 - x, line) for x in range(h)]][
            0] if False else None
        if d in "NS":
            cells = [(line, y) for y in (range(h) if d == "N" else range(h - 1, -1, -1))]
        else:
            cells = [(x, line) for x in (range(w) if d == "W" else range(w - 1, -1, -1))]
        target = 0
        for x, y in cells:
            if g[y][x] == "#":
                target = (cells.index((x, y)) + 1)
            elif g[y][x] == "O":
                tx, ty = cells[target];
                target += 1
                if (tx, ty) != (x, y): g[ty][tx] = "O";g[y][x] = "."
    return tuple("".join(r) for r in g)


def load(g): return sum((len(g) - y) * r.count("O") for y, r in enumerate(g))


def cycle(g):
    for d in "NWSE": g = tilt(g, d)
    return g


def solve(d, n):
    g = tuple(d.splitlines());
    seen = {};
    i = 0
    while i < n:
        if g in seen:
            cycle_len = i - seen[g];
            skip = (n - i) // cycle_len
            if skip: i += skip * cycle_len
            if i >= n: break
        else:
            seen[g] = i
        g = cycle(g);
        i += 1
    return load(g)


def part1(d): return load(tilt(tuple(d.splitlines()), "N"))


def part2(d): return solve(d, 1_000_000_000)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
