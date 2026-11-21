from pathlib import Path


def part1(data: str) -> int:
    step = int(data.strip())
    buffer = [0]
    position = 0
    for value in range(1, 2018):
        position = (position + step) % len(buffer) + 1
        buffer.insert(position, value)
    return buffer[(buffer.index(2017) + 1) % len(buffer)]


def part2(data: str, insertions: int = 50_000_000) -> int:
    step = int(data.strip())
    position = value_after_zero = 0
    for value in range(1, insertions + 1):
        position = (position + step) % value + 1
        if position == 1:
            value_after_zero = value
    return value_after_zero


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
