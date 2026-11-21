from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from intcode import Computer


def run(data: str, value: int) -> int:
    output = Computer(list(map(int, data.strip().split(","))), [value]).run()
    if not output: raise ValueError("Program produced no output")
    return output[-1]


def part1(data: str) -> int: return run(data, 1)


def part2(data: str) -> int: return run(data, 5)


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
