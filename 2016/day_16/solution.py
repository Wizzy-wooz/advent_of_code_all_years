
def checksum(data: str, length: int) -> str:
    bits = data.strip()
    while len(bits) < length:
        bits += '0' + ''.join('1' if c == '0' else '0' for c in bits[::-1])
    bits = bits[:length]
    while len(bits) % 2 == 0:
        bits = ''.join('1' if bits[i] == bits[i+1] else '0' for i in range(0, len(bits), 2))
    return bits


def part1(data: str) -> str: return checksum(data, 272)
def part2(data: str) -> str: return checksum(data, 35651584)


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
