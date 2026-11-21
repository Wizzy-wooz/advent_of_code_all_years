from pathlib import Path


def seat(s): return int(s.translate(str.maketrans("FBLR", "0101")), 2)


def seats(d): return [seat(x.strip()) for x in d.splitlines() if x.strip()]


def part1(d): return max(seats(d))


def part2(d):
    ss = set(seats(d));
    return next(i for i in range(min(ss), max(ss)) if i not in ss and i - 1 in ss and i + 1 in ss)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
