from pathlib import Path

SHAPES = ((0, 1, 2, 3), (1, 4, 5, 6, 9), (0, 1, 2, 6, 10), (0, 4, 8, 12), (0, 1, 4, 5))


def height(d, target):
    jets = d.strip();
    rows = [127];
    ji = 0;
    rock = 0;
    added = 0;
    seen = {}
    while rock < target:
        shape = SHAPES[rock % 5];
        x = 2;
        y = len(rows) + 3

        def occupied(xx, yy):
            return any(xx + ((p % 4)) < 0 or xx + (p % 4) >= 7 or (
                        (p // 4) + yy < len(rows) and rows[(p // 4) + yy] >> (xx + p % 4) & 1) for p in shape)

        while True:
            dx = 1 if jets[ji % len(jets)] == ">" else -1;
            ji += 1
            if not occupied(x + dx, y): x += dx
            if occupied(x, y - 1): break
            y -= 1
        for p in shape:
            xx = x + p % 4;
            yy = y + p // 4
            while len(rows) <= yy: rows.append(0)
            rows[yy] |= 1 << xx
        rock += 1
        top = len(rows) - 1
        while top > 0 and rows[top] == 0: top -= 1
        key = (rock % 5, ji % len(jets), tuple(rows[max(1, top - 30):top + 1]))
        if key in seen and rock < target:
            oldr, oldh = seen[key];
            cycle = rock - oldr;
            dh = top - oldh;
            n = (target - rock) // cycle
            if n: rock += n * cycle;added += n * dh
        else:
            seen[key] = (rock, top)
    return len(rows) - 1 + added


def part1(d): return height(d, 2022)


def part2(d): return height(d, 1_000_000_000_000)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
