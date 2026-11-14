
def safe_count(first_row: str, rows: int) -> int:
    row = first_row.strip(); total = 0
    for _ in range(rows):
        total += row.count('.')
        row = ''.join('^' if (row[i-1] if i else '.') != (row[i+1] if i+1 < len(row) else '.') else '.' for i in range(len(row)))
    return total


def part1(data: str) -> int: return safe_count(data, 40)
def part2(data: str) -> int: return safe_count(data, 400000)


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
