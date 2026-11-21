from collections import Counter
from math import prod, sqrt
from pathlib import Path


def rotate(g): return tuple("".join(row) for row in zip(*g[::-1]))


def variants(g):
    out = set();
    g = tuple(g)
    for _ in range(4): out.add(g);out.add(tuple(r[::-1] for r in g));g = rotate(g)
    return out


def assemble(d):
    tiles = {int(block.splitlines()[0][5:-1]): tuple(block.splitlines()[1:]) for block in d.strip().split("\n\n")};
    n = int(sqrt(len(tiles)));
    edge_count = Counter()
    for g in tiles.values():
        for e in (g[0], g[-1], "".join(r[0] for r in g), "".join(r[-1] for r in g)): edge_count[min(e, e[::-1])] += 1

    def unique(e):
        return edge_count[min(e, e[::-1])] == 1

    options = {i: list(variants(g)) for i, g in tiles.items()};
    board = [None] * (n * n);
    used = set()

    def search(pos):
        if pos == n * n: return True
        r, c = divmod(pos, n);
        top = board[pos - n][1][-1] if r else None;
        left = "".join(row[-1] for row in board[pos - 1][1]) if c else None
        for tid, forms in options.items():
            if tid in used: continue
            for g in forms:
                edges = (g[0], g[-1], "".join(row[0] for row in g), "".join(row[-1] for row in g))
                if top is not None and top != edges[0]: continue
                if left is not None and left != edges[2]: continue
                if (r == 0) != unique(edges[0]) or (r == n - 1) != unique(edges[1]) or (c == 0) != unique(edges[2]) or (
                        c == n - 1) != unique(edges[3]): continue
                board[pos] = (tid, g);
                used.add(tid)
                if search(pos + 1): return True
                used.remove(tid);
                board[pos] = None
        return False

    if not search(0): raise ValueError("Could not assemble tile image")
    return n, board


def solve(d):
    n, b = assemble(d);
    corner = prod(b[i][0] for i in (0, n - 1, n * (n - 1), n * n - 1));
    image = []
    for r in range(n):
        for inner in range(1, len(b[0][1]) - 1): image.append("".join(b[r * n + c][1][inner][1:-1] for c in range(n)))
    monsters = ("                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   ")
    total = sum(row.count("#") for row in image)
    best = total
    for g in variants(tuple(image)):
        h = len(g);
        w = len(g[0]);
        found = set()
        for y in range(h - 2):
            for x in range(w - 19):
                points = {(x + dx, y + dy) for dy, row in enumerate(monsters) for dx, ch in enumerate(row) if ch == "#"}
                if all(g[py][px] == "#" for px, py in points): found |= points
        best = min(best, total - len(found))
    return corner, best


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
