from pathlib import Path


def solve(d):
    a, b = d.strip().split("\n\n");
    ranges = sorted(tuple(map(int, x.split("-"))) for x in a.splitlines());
    merged = []
    for lo, hi in ranges:
        if merged and lo <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
        else:
            merged.append((lo, hi))
    ids = list(map(int, b.split()));
    return sum(any(a <= n <= z for a, z in merged) for n in ids), sum(z - a + 1 for a, z in merged)


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
