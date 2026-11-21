from pathlib import Path


def fuel(mass: int) -> int: return max(mass // 3 - 2, 0)


def part1(data: str) -> int: return sum(fuel(int(x)) for x in data.split())


def part2(data: str) -> int:
    total = 0
    for mass in map(int, data.split()):
        while mass := fuel(mass): total += mass
    return total


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
