import re


def screen(data: str, width: int = 50, height: int = 6) -> list[list[bool]]:
    grid = [[False] * width for _ in range(height)]
    for line in data.splitlines():
        if m := re.fullmatch(r'rect (\d+)x(\d+)', line):
            w, h = map(int, m.groups())
            for y in range(h):
                for x in range(w): grid[y][x] = True
        elif m := re.fullmatch(r'rotate row y=(\d+) by (\d+)', line):
            y, n = map(int, m.groups()); n %= width
            grid[y] = grid[y][-n:] + grid[y][:-n] if n else grid[y]
        elif m := re.fullmatch(r'rotate column x=(\d+) by (\d+)', line):
            x, n = map(int, m.groups()); n %= height
            col = [grid[y][x] for y in range(height)]; col = col[-n:] + col[:-n] if n else col
            for y in range(height): grid[y][x] = col[y]
    return grid


def part1(data: str) -> int: return sum(map(sum, screen(data)))
def part2(data: str) -> str: return '\n'.join(''.join('#' if p else ' ' for p in row) for row in screen(data))


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2:\n{part2(data)}')
