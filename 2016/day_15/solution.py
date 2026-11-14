import re
from math import lcm


def solve(data: str, extra: bool = False) -> int:
    discs = []
    for line in data.splitlines():
        if not line.strip():
            continue
        match = re.search(r'has (\d+) positions;.*position (\d+)\.', line)
        if match is None:
            raise ValueError(f'Invalid disc description: {line!r}')
        discs.append(tuple(map(int, match.groups())))
    # Parsed values are (positions, starting position); disc number is its input order.
    if extra: discs.append((11, 0))
    t, step = 0, 1
    for i, (positions, start) in enumerate(discs, 1):
        while (start + t + i) % positions: t += step
        step = lcm(step, positions)
    return t


def part1(data: str) -> int: return solve(data)
def part2(data: str) -> int: return solve(data, True)


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
