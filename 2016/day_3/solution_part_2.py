from pathlib import Path


def is_triangle(sides: list[int]) -> bool:
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a


def solve(rows: list[list[int]]) -> int:
    triangle_count = 0

    # Read three rows at a time. Each column makes one triangle.
    for i in range(0, len(rows), 3):
        group = rows[i:i + 3]
        for column in range(3):
            sides = [group[row][column] for row in range(3)]
            if is_triangle(sides):
                triangle_count += 1

    return triangle_count


if __name__ == '__main__':
    input_path = Path(__file__).with_name('input_part_2.txt')
    rows = [list(map(int, line.split())) for line in input_path.read_text().splitlines()]
    print(f'Part 2: {solve(rows)}')
