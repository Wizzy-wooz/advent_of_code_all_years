from pathlib import Path


def solve(d):
    g = d.splitlines();
    h = len(g);
    w = len(g[0]);
    a = b = 0
    for y in range(h):
        for x in range(w):
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                a += "".join(g[y + i * dy][x + i * dx] for i in range(4) if
                             0 <= x + i * dx < w and 0 <= y + i * dy < h) == "XMAS" and all(
                    0 <= x + i * dx < w and 0 <= y + i * dy < h for i in range(4))
            if 0 < x < w - 1 and 0 < y < h - 1 and g[y][x] == "A": b += (
                        {g[y - 1][x - 1], g[y + 1][x + 1]} == {"M", "S"} and {g[y - 1][x + 1], g[y + 1][x - 1]} == {"M",
                                                                                                                    "S"})
    return a, b


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
