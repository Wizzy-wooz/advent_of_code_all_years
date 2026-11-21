from pathlib import Path
import re


def reservoir(data: str) -> tuple[int, int]:
    clay = set()
    for line in data.splitlines():
        if not line.strip():
            continue

        veins = re.findall(r"([xy])=(-?\d+)(?:\.\.(-?\d+))?", line)
        if len(veins) != 2:
            raise ValueError(f"Invalid clay vein: {line}")

        fixed_axis, fixed_value, _ = veins[0]
        range_axis, range_start, range_end = veins[1]
        fixed = int(fixed_value)
        start = int(range_start)
        end = int(range_end or range_start)

        for value in range(start, end + 1):
            if fixed_axis == "x":
                clay.add((fixed, value))
            else:
                clay.add((value, fixed))

    min_y = min(y for _, y in clay)
    max_y = max(y for _, y in clay)
    flowing = set()
    settled = set()
    sources = [(500, 0)]

    def supported(x: int, y: int) -> bool:
        return (x, y) in clay or (x, y) in settled

    while sources:
        x, y = sources.pop()

        while 0 <= y <= max_y:
            if supported(x, y):
                break

            while y <= max_y and not supported(x, y) and not supported(x, y + 1):
                flowing.add((x, y))
                y += 1

            if y > max_y or supported(x, y):
                break

            flowing.add((x, y))

            left = x
            while (left - 1, y) not in clay:
                left -= 1
                flowing.add((left, y))
                if not supported(left, y + 1):
                    break

            right = x
            while (right + 1, y) not in clay:
                right += 1
                flowing.add((right, y))
                if not supported(right, y + 1):
                    break

            left_wall = (left - 1, y) in clay
            right_wall = (right + 1, y) in clay

            if left_wall and right_wall:
                for water_x in range(left, right + 1):
                    settled.add((water_x, y))
                    flowing.discard((water_x, y))
                y -= 1
                continue

            if not left_wall:
                sources.append((left, y))
            if not right_wall:
                sources.append((right, y))
            break

    reached = flowing | settled
    return (
        sum(min_y <= y <= max_y for _, y in reached),
        sum(min_y <= y <= max_y for _, y in settled),
    )


def part1(data: str) -> int:
    return reservoir(data)[0]


def part2(data: str) -> int:
    return reservoir(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
