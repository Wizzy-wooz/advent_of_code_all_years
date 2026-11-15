from pathlib import Path


def part1(target: int) -> int:
    if target < 1:
        raise ValueError("Spiral memory positions start at 1")

    x = y = 0
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    direction = 0
    run_length = 1
    position = 1

    while position < target:
        for _ in range(2):
            dx, dy = directions[direction]
            for _ in range(run_length):
                if position == target:
                    return abs(x) + abs(y)
                x += dx
                y += dy
                position += 1
            direction = (direction + 1) % 4
        run_length += 1

    return abs(x) + abs(y)


def part2(target: int) -> int:
    if target < 1:
        raise ValueError("Spiral memory values must be positive")

    values = {(0, 0): 1}
    x = y = 0
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    direction = 0
    run_length = 1

    while True:
        for _ in range(2):
            dx, dy = directions[direction]
            for _ in range(run_length):
                x += dx
                y += dy
                value = sum(
                    values.get((x + offset_x, y + offset_y), 0)
                    for offset_x in (-1, 0, 1)
                    for offset_y in (-1, 0, 1)
                    if offset_x or offset_y
                )
                if value > target:
                    return value
                values[(x, y)] = value
            direction = (direction + 1) % 4
        run_length += 1


if __name__ == "__main__":
    target = int(Path(__file__).with_name("input.txt").read_text().strip())
    print("Part 1:", part1(target))
    print("Part 2:", part2(target))
