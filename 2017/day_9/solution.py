from pathlib import Path


def score_and_garbage(data: str) -> tuple[int, int]:
    depth = score = garbage_count = 0
    in_garbage = cancelled = False
    for char in data.strip():
        if cancelled:
            cancelled = False
        elif char == "!" and in_garbage:
            cancelled = True
        elif in_garbage:
            if char == ">":
                in_garbage = False
            else:
                garbage_count += 1
        elif char == "<":
            in_garbage = True
        elif char == "{":
            depth += 1
            score += depth
        elif char == "}":
            depth -= 1
    return score, garbage_count


def part1(data: str) -> int:
    return score_and_garbage(data)[0]


def part2(data: str) -> int:
    return score_and_garbage(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
