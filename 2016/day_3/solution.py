from pathlib import Path


def is_triangle(sides: list[int]) -> bool:
    a, b, c = sorted(sides)
    return a + b > c


def part1(data: str) -> int:
    return sum(is_triangle(list(map(int, line.split()))) for line in data.splitlines() if line.strip())


def part2(data: str) -> int:
    rows = [list(map(int, line.split())) for line in data.splitlines() if line.strip()]
    if len(rows) % 3:
        raise ValueError('Vertical triangle input must have a multiple of three rows')
    return sum(
        is_triangle([rows[i][column], rows[i + 1][column], rows[i + 2][column]])
        for i in range(0, len(rows), 3)
        for column in range(3)
    )


if __name__ == '__main__':
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
