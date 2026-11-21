from pathlib import Path


def spoken(d, target):
    start = list(map(int, d.strip().split(",")));
    last = {n: i + 1 for i, n in enumerate(start[:-1])};
    n = start[-1]
    for turn in range(len(start), target): prev = last.get(n, 0);last[n] = turn;n = 0 if not prev else turn - prev
    return n


def part1(d): return spoken(d, 2020)


def part2(d): return spoken(d, 30_000_000)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
