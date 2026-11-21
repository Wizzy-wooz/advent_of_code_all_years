from pathlib import Path


def fish(d, days):
    a = [0] * 9
    for n in map(int, d.strip().split(",")): a[n] += 1
    for _ in range(days): a = a[1:] + [a[0]];a[6] += a[8]
    return sum(a)


def part1(d): return fish(d, 80)


def part2(d): return fish(d, 256)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
