from pathlib import Path


def run(d, wide=False):
    a, b = d.split("\n\n");
    g = [list(r) for r in a.splitlines()];
    moves = "".join(b.split());
    if wide:
        g = [[c for x in row for c in ({"#": "##", ".": "..", "O": "[]", "@": "@."}[x])] for row in g]
    x = next(x for y, r in enumerate(g) for x, c in enumerate(r) if c == "@");
    y = next(y for y, r in enumerate(g) if "@" in r);
    g[y][x] = ".";
    dirs = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

    def box(x, y):
        return (x - 1 if g[y][x] == "]" else x, y)

    for m in moves:
        dx, dy = dirs[m];
        nx, ny = x + dx, y + dy;
        c = g[ny][nx]
        if c == "#": continue
        if c == ".": x, y = nx, ny;continue
        if not wide:
            tx, ty = nx, ny
            while g[ty][tx] not in "#.": tx += dx;ty += dy
            if g[ty][tx] == "#": continue
            while (tx, ty) != (nx, ny): g[ty][tx] = g[ty - dy][tx - dx];tx -= dx;ty -= dy
            g[ny][nx] = ".";
            x, y = nx, ny;
            continue
        boxes = {box(nx, ny)};
        todo = list(boxes);
        valid = True
        while todo:
            bx, by = todo.pop()
            for cx in (bx, bx + 1):
                tx, ty = cx + dx, by + dy;
                ch = g[ty][tx]
                if ch == "#":
                    valid = False
                elif ch in "[]":
                    other = box(tx, ty)
                    if other not in boxes: boxes.add(other);todo.append(other)
        if not valid: continue
        for bx, by in sorted(boxes, key=lambda p: p[1] * dy + p[0] * dx, reverse=True): g[by][bx] = g[by][bx + 1] = "."
        for bx, by in boxes: g[by + dy][bx + dx] = "[";g[by + dy][bx + dx + 1] = "]"
        x, y = nx, ny
    return sum(100 * y + x for y, r in enumerate(g) for x, c in enumerate(r) if c == ("[" if wide else "O"))


def part1(d): return run(d)


def part2(d): return run(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
