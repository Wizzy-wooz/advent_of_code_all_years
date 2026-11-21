from pathlib import Path


def reachable(g, steps, infinite=False):
    h = len(g);
    w = len(g[0]);
    s = next((x, y) for y, r in enumerate(g) for x, c in enumerate(r) if c == "S");
    front = {s}
    for _ in range(steps):
        front = {(x + dx, y + dy) for x, y in front for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)) if (
            g[(y + dy) % h][(x + dx) % w] != "#" if infinite else 0 <= x + dx < w and 0 <= y + dy < h and g[y + dy][
                x + dx] != "#")}
    return len(front)


def part1(d): return reachable(d.splitlines(), 64)


def part2(d):
    g = d.splitlines();
    target = 26501365;
    period = len(g);
    r = target % period
    vals = [reachable(g, r + k * period, True) for k in range(3)];
    n = (target - r) // period
    return vals[0] + n * (vals[1] - vals[0]) + n * (n - 1) // 2 * (vals[2] - 2 * vals[1] + vals[0])


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
