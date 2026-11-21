from pathlib import Path


def fold(d):
    a, b = d.split("\n\n");
    pts = {tuple(map(int, x.split(","))) for x in a.splitlines()};
    instructions = [x.rsplit("=", 1) for x in b.splitlines() if x]
    first = None
    for axis, n in instructions:
        n = int(n);
        pts = {(2 * n - x if axis.endswith("x") and x > n else x, 2 * n - y if axis.endswith("y") and y > n else y) for
               x, y in pts}
        if first is None: first = len(pts)
    return first if first is not None else len(pts), "\n".join(
        "".join("#" if (x, y) in pts else " " for x in range(max(a for a, b in pts) + 1)).rstrip() for y in
        range(max(b for a, b in pts) + 1))


def part1(d): return fold(d)[0]


def part2(d): return fold(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:\n" + part2(d))
