from collections import Counter


def decode(data: str, least: bool = False) -> str:
    rows = [line.strip() for line in data.splitlines() if line.strip()]
    if not rows or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError('Expected a non-empty rectangular message')
    decoded = []
    for column in zip(*rows):
        counts = Counter(column)
        decoded.append(sorted(counts, key=lambda char: (counts[char] if least else -counts[char], char))[0])
    return ''.join(decoded)


def part1(data: str) -> str: return decode(data)
def part2(data: str) -> str: return decode(data, True)


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
