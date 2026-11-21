from pathlib import Path
import re


def part1(d): return sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", d))


def part2(d):
    enabled = True;
    total = 0
    for m in re.finditer(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)", d):
        if m[0] == "do()":
            enabled = True
        elif m[0] == "don't()":
            enabled = False
        elif enabled:
            total += int(m[1]) * int(m[2])
    return total


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
