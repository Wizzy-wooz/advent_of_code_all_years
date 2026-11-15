from pathlib import Path


def count_steps(offsets: list[int], strange_rules: bool = False) -> int:
    instructions = offsets.copy()
    position = steps = 0

    while 0 <= position < len(instructions):
        jump = instructions[position]
        if strange_rules and jump >= 3:
            instructions[position] -= 1
        else:
            instructions[position] += 1
        position += jump
        steps += 1

    return steps


def part1(data: str) -> int:
    offsets = [int(line) for line in data.splitlines() if line.strip()]
    return count_steps(offsets)


def part2(data: str) -> int:
    offsets = [int(line) for line in data.splitlines() if line.strip()]
    return count_steps(offsets, strange_rules=True)


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
