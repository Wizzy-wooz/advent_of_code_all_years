from functools import lru_cache
from pathlib import Path

NUM = {"7": (0, 0), "8": (1, 0), "9": (2, 0), "4": (0, 1), "5": (1, 1), "6": (2, 1), "1": (0, 2), "2": (1, 2),
       "3": (2, 2), "0": (1, 3), "A": (2, 3)}
DIR = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}


def shortest_commands(a, b, pad):
    pos = NUM if pad == 0 else DIR;
    valid = set(pos.values());
    x, y = pos[a];
    tx, ty = pos[b];
    q = [(x, y, "")];
    out = [];
    best = None
    for cx, cy, s in q:
        if best is not None and len(s) > best: continue
        if (cx, cy) == (tx, ty): best = len(s);out.append(s + "A");continue
        for c, (dx, dy) in (("<", (-1, 0)), (">", (1, 0)), ("^", (0, -1)), ("v", (0, 1))):
            n = (cx + dx, cy + dy)
            gap = (0, 3) if pad == 0 else (0, 0)
            if n in valid and n != gap: q.append((n[0], n[1], s + c))
    return out


@lru_cache(None)
def cost(seq, depth):
    if depth == 0: return len(seq)
    total = 0;
    cur = "A"
    for c in seq: total += min(cost(path, depth - 1) for path in shortest_commands(cur, c, 1));cur = c
    return total


def solve(d, depth):
    total = 0
    for code in d.splitlines():
        if code.strip():
            seqs = [""];
            cur = "A"
            for c in code:
                seqs = [s + p for s in seqs for p in shortest_commands(cur, c, 0)];
                cur = c
            total += int(code[:-1]) * min(cost(s, depth) for s in seqs)
    return total


def part1(d): return solve(d, 2)


def part2(d): return solve(d, 25)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
