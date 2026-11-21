from pathlib import Path


def step(grid):
    out = set()
    for y in range(5):
        for x in range(5):
            n = sum((nx, ny) in grid for nx, ny in ((x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)))
            if (x, y) in grid and n == 1 or (x, y) not in grid and n in (1, 2): out.add((x, y))
    return out


def part1(data):
    g = {(x, y) for y, r in enumerate(data.splitlines()) for x, c in enumerate(r) if c == "#"};
    seen = set()
    while frozenset(g) not in seen: seen.add(frozenset(g));g = step(g)
    return sum(1 << (y * 5 + x) for x, y in g)


def part2(data, minutes=200):
    bugs = {(x, y, 0) for y, r in enumerate(data.splitlines()) for x, c in enumerate(r) if
            c == "#" and (x, y) != (2, 2)}
    for _ in range(minutes):
        nxt = set();
        levels = [z for _, _, z in bugs]
        for z in range(min(levels, default=0) - 1, max(levels, default=0) + 2):
            for y in range(5):
                for x in range(5):
                    if (x, y) == (2, 2): continue
                    neighbors = []
                    for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
                        nx, ny = x + dx, y + dy
                        if (nx, ny) == (2, 2):
                            if x == 1:
                                neighbors.extend((0, yy, z + 1) for yy in range(5))
                            elif x == 3:
                                neighbors.extend((4, yy, z + 1) for yy in range(5))
                            elif y == 1:
                                neighbors.extend((xx, 0, z + 1) for xx in range(5))
                            else:
                                neighbors.extend((xx, 4, z + 1) for xx in range(5))
                        elif nx < 0:
                            neighbors.append((1, 2, z - 1))
                        elif nx > 4:
                            neighbors.append((3, 2, z - 1))
                        elif ny < 0:
                            neighbors.append((2, 1, z - 1))
                        elif ny > 4:
                            neighbors.append((2, 3, z - 1))
                        else:
                            neighbors.append((nx, ny, z))
                    count = sum(p in bugs for p in neighbors)
                    if (x, y, z) in bugs and count == 1 or (x, y, z) not in bugs and count in (1, 2): nxt.add((x, y, z))
        bugs = nxt
    return len(bugs)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
