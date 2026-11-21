from pathlib import Path


def totals(d): return sorted((sum(map(int, g.split())) for g in d.strip().split("\n\n")), reverse=True)


def part1(d): return totals(d)[0]


def part2(d): return sum(totals(d)[:3])


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
