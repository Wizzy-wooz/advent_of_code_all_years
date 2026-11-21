from pathlib import Path


def pairs(d):
    for line in d.splitlines():
        if line.strip(): a, b = line.split(",");x, y = map(int, a.split("-"));u, v = map(int,
                                                                                         b.split("-"));yield x, y, u, v


def part1(d): return sum((x <= u and y >= v) or (u <= x and v >= y) for x, y, u, v in pairs(d))


def part2(d): return sum(max(x, u) <= min(y, v) for x, y, u, v in pairs(d))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
