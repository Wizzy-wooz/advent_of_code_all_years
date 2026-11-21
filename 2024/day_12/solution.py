from pathlib import Path


def solve(d):
    g = d.splitlines();
    h = len(g);
    w = len(g[0]);
    seen = set();
    p1 = p2 = 0
    for y in range(h):
        for x in range(w):
            if (x, y) in seen: continue
            char = g[y][x];
            region = {(x, y)};
            stack = [(x, y)];
            seen.add((x, y));
            per = 0;
            edges = set()
            while stack:
                a, b = stack.pop()
                for dx, dy, side in ((0, -1, "N"), (1, 0, "E"), (0, 1, "S"), (-1, 0, "W")):
                    n = (a + dx, b + dy)
                    if not (0 <= n[0] < w and 0 <= n[1] < h) or g[n[1]][n[0]] != char:
                        per += 1;edges.add((a, b, side))
                    elif n not in seen:
                        seen.add(n);region.add(n);stack.append(n)
            # Count boundary runs by testing the preceding edge along each side's axis.
            sides = sum((x, y - 1, s) not in edges if s in "EW" else (x - 1, y, s) not in edges for x, y, s in edges)
            p1 += len(region) * per;
            p2 += len(region) * sides
    return p1, p2


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
