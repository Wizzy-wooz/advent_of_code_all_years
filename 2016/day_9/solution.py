import re


def decompressed_length(data: str, recursive: bool = False) -> int:
    data = ''.join(data.split())
    total = i = 0
    while i < len(data):
        if data[i] != '(': total += 1; i += 1; continue
        m = re.match(r'\((\d+)x(\d+)\)', data[i:])
        if not m: raise ValueError(f'Invalid marker at offset {i}')
        size, repeats = map(int, m.groups()); start = i + m.end()
        segment = data[start:start + size]
        total += (decompressed_length(segment, True) if recursive else size) * repeats
        i = start + size
    return total


def part1(data: str) -> int: return decompressed_length(data)
def part2(data: str) -> int: return decompressed_length(data, True)


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
