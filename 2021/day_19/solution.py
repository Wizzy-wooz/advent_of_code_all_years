from collections import Counter
from itertools import permutations, product
from pathlib import Path


def rotations(p):
    for axes in permutations(range(3)):
        inversions = sum(axes[i] > axes[j] for i in range(3) for j in range(i + 1, 3))
        parity = -1 if inversions % 2 else 1
        for signs in product((1, -1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] > 0:
                yield tuple(signs[i] * p[axes[i]] for i in range(3))


def parse(d): return [[tuple(map(int, l.split(","))) for l in b.splitlines()[1:]] for b in d.strip().split("\n\n")]


def solve(d):
    scanners = parse(d);
    located = {0: set(scanners[0])};
    positions = {0: (0, 0, 0)};
    todo = set(range(1, len(scanners)))
    while todo:
        progress = False
        for i in list(todo):
            for known in located.values():
                found = False
                for rot in zip(*[rotations(p) for p in scanners[i]]):
                    offsets = Counter(tuple(a[k] - b[k] for k in range(3)) for a in known for b in rot);
                    off, n = offsets.most_common(1)[0]
                    if n >= 12:
                        located[i] = {tuple(p[k] + off[k] for k in range(3)) for p in rot};
                        positions[i] = off;
                        todo.remove(i);
                        progress = found = True;
                        break
                    if found: break
                if found: break
        if not progress: raise ValueError("Could not align all scanners")
    beacons = set.union(*located.values());
    dist = max(sum(abs(a[k] - b[k]) for k in range(3)) for a in positions.values() for b in positions.values())
    return len(beacons), dist


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
