from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]));
from intcode import Computer


def beam(program, x, y): return Computer(program, [x, y]).run()[0]


def part1(data):
    p = list(map(int, data.strip().split(",")));
    return sum(beam(p, x, y) for y in range(50) for x in range(50))


def part2(data):
    p = list(map(int, data.strip().split(",")));
    x = y = 0
    while True:
        while not beam(p, x, y): x += 1
        if beam(p, x + 99, y - 99): return x * 10000 + (y - 99)
        y += 1


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
