from pathlib import Path


def groups(d): return [p.split() for p in d.strip().split("\n\n") if p.strip()]


def part1(d): return sum(len(set.union(*(set(x) for x in g))) for g in groups(d))


def part2(d): return sum(len(set.intersection(*(set(x) for x in g))) for g in groups(d))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
