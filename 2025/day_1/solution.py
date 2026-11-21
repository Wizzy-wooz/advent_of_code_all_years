from pathlib import Path
import re


def solve(data: str) -> tuple[int, int]:
    position = 50
    landed_on_zero = crossings = 0
    for turn in re.findall(r"[LR]\d+", data):
        direction, amount = turn[0], int(turn[1:])
        step = 1 if direction == "R" else -1
        for _ in range(amount):
            position = (position + step) % 100
            crossings += position == 0
        landed_on_zero += position == 0
    return landed_on_zero, crossings


def part1(data: str) -> int: return solve(data)[0]


def part2(data: str) -> int: return solve(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
