from collections import Counter
from pathlib import Path


def run(d, rounds=None):
    elves = {(x, y) for y, r in enumerate(d.splitlines()) for x, c in enumerate(r) if c == "#"};
    checks = [((-1, -1), (0, -1), (1, -1)), ((-1, 1), (0, 1), (1, 1)), ((-1, -1), (-1, 0), (-1, 1)),
              ((1, -1), (1, 0), (1, 1))];
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)];
    r = 0
    while rounds is None or r < rounds:
        props = {};
        counts = Counter()
        for x, y in elves:
            if not any((x + dx, y + dy) in elves for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx or dy): continue
            for k in range(4):
                i = (r + k) % 4
                if all((x + dx, y + dy) not in elves for dx, dy in checks[i]):
                    dx, dy = dirs[i];
                    p = (x + dx, y + dy);
                    props[(x, y)] = p;
                    counts[p] += 1;
                    break
        nxt = {props.get(e, e) if counts[props.get(e, e)] == 1 else e for e in elves};
        r += 1
        if nxt == elves and rounds is None: return r, 0
        elves = nxt
        if r == 10:
            xs = [x for x, y in elves];
            ys = [y for x, y in elves];
            area = (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1) - len(elves)
            if rounds == 10: return r, area
    return r, area


def part1(d): return run(d, 10)[1]


def part2(d): return run(d, None)[0]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
