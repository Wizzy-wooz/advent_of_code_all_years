from pathlib import Path


def power(x: int, y: int, serial: int) -> int:
    rack = x + 10
    return ((rack * y + serial) * rack // 100) % 10 - 5


def summed(serial: int):
    grid = [[0] * 301 for _ in range(301)]
    for y in range(1, 301):
        for x in range(1, 301):
            grid[y][x] = power(x, y, serial) + grid[y - 1][x] + grid[y][x - 1] - grid[y - 1][x - 1]
    return grid


def best_square(serial: int, sizes=range(1, 301)) -> tuple[int, int, int, int]:
    grid = summed(serial);
    best = (0, 0, 0, -10 ** 9)
    for size in sizes:
        for y in range(1, 302 - size):
            for x in range(1, 302 - size):
                total = grid[y + size - 1][x + size - 1] - grid[y - 1][x + size - 1] - grid[y + size - 1][x - 1] + \
                        grid[y - 1][x - 1]
                if total > best[3]: best = (x, y, size, total)
    return best


def part1(data: str) -> str:
    x, y, _, _ = best_square(int(data.strip()), (3,));
    return f"{x},{y}"


def part2(data: str) -> str:
    x, y, size, _ = best_square(int(data.strip()));
    return f"{x},{y},{size}"


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
