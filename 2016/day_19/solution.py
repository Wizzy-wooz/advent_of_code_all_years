
def part1(data: str) -> int:
    n = int(data.strip()); power = 1
    while power * 2 <= n: power *= 2
    return 2 * (n - power) + 1


def part2(data: str) -> int:
    n = int(data.strip()); power = 1
    while power * 3 <= n: power *= 3
    if n == power: return n
    if n <= 2 * power: return n - power
    return 2 * n - 3 * power


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
