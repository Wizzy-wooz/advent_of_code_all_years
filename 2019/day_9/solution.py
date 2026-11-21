from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]));
from intcode import Computer


def run(data, value): return Computer(list(map(int, data.strip().split(","))), [value]).run()[-1]


def part1(data): return run(data, 1)


def part2(data): return run(data, 2)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
