from pathlib import Path


def accessible(grid, at):
    x, y = at
    return sum(
        0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid) and grid[y + dy][x + dx] == "@" for dx in (-1, 0, 1) for
        dy in (-1, 0, 1) if dx or dy) < 4


def solve(d):
    grid = [list(r) for r in d.splitlines() if r];
    first = sum(accessible(grid, (x, y)) for y, r in enumerate(grid) for x, c in enumerate(r) if c == "@");
    removed = 0
    while True:
        now = [(x, y) for y, r in enumerate(grid) for x, c in enumerate(r) if c == "@" and accessible(grid, (x, y))]
        if not now: break
        for x, y in now: grid[y][x] = "."
        removed += len(now)
    return first, removed


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
