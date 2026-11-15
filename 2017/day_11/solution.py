from pathlib import Path


DELTAS = {"n": (0, 1), "ne": (1, 0), "se": (1, -1), "s": (0, -1), "sw": (-1, 0), "nw": (-1, 1)}


def distances(data: str) -> tuple[int, int]:
    x = y = greatest = 0
    for direction in filter(None, data.strip().split(",")):
        dx, dy = DELTAS[direction]
        x += dx
        y += dy
        greatest = max(greatest, (abs(x) + abs(y) + abs(x + y)) // 2)
    return (abs(x) + abs(y) + abs(x + y)) // 2, greatest


def part1(data: str) -> int:
    return distances(data)[0]


def part2(data: str) -> int:
    return distances(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
