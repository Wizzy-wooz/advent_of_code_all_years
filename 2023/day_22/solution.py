from collections import defaultdict
from pathlib import Path


def settle(d):
    bricks = []
    for i, line in enumerate(d.splitlines()):
        if line.strip(): a, b = line.split("~");x1, y1, z1 = map(int, a.split(","));x2, y2, z2 = map(int, b.split(
            ","));bricks.append([i, min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2), min(z1, z2), max(z1, z2)])
    bricks.sort(key=lambda b: b[5]);
    top = {};
    supports = defaultdict(set);
    above = defaultdict(set)
    for b in bricks:
        i, x1, x2, y1, y2, z1, z2 = b;
        floor = max((top.get((x, y), (0, None))[0] for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)), default=0)
        beneath = {top[(x, y)][1] for x in range(x1, x2 + 1) for y in range(y1, y2 + 1) if
                   top.get((x, y), (0, None))[0] == floor and top.get((x, y), (0, None))[1] is not None}
        supports[i] = beneath
        for j in beneath: above[j].add(i)
        newz = floor + 1;
        height = z2 - z1;
        b[5] = newz;
        b[6] = newz + height
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1): top[(x, y)] = (b[6], i)
    safe = sum(all(len(supports[j]) > 1 for j in above[i]) for i, _, _, _, _, _, _ in bricks);
    total = 0
    for b, *_ in bricks:
        gone = {b};
        q = [b]
        while q:
            x = q.pop()
            for y in above[x]:
                if supports[y] <= gone and y not in gone: gone.add(y);q.append(y)
        total += len(gone) - 1
    return safe, total


def part1(d): return settle(d)[0]


def part2(d): return settle(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
