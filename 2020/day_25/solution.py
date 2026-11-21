from pathlib import Path

MOD = 20201227


def part1(d):
    a, b = map(int, d.split());
    value = 1;
    loop = 0
    while value != a: value = value * 7 % MOD;loop += 1
    return pow(b, loop, MOD)


def part2(d): return "Merry Christmas!"


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
