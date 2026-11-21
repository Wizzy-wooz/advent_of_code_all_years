from pathlib import Path


def react(polymer: str) -> str:
    stack = []
    for unit in polymer.strip():
        if stack and stack[-1] != unit and stack[-1].lower() == unit.lower():
            stack.pop()
        else:
            stack.append(unit)
    return "".join(stack)


def part1(data: str) -> int: return len(react(data))


def part2(data: str) -> int:
    polymer = data.strip()
    return min(len(react("".join(c for c in polymer if c.lower() != unit))) for unit in "abcdefghijklmnopqrstuvwxyz")


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
