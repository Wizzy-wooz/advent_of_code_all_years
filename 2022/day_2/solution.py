from pathlib import Path


def score(d, part2=False):
    total = 0
    for line in d.splitlines():
        if not line.strip(): continue
        a, b = line.split();
        x = ord(a) - 65;
        y = ord(b) - 88
        if part2: y = (x + y - 1) % 3
        total += y + 1 + (3 if y == x else 6 if (y - x) % 3 == 1 else 0)
    return total


def part1(d): return score(d)


def part2(d): return score(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
