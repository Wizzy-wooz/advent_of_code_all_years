import re
from pathlib import Path


COMMAND = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')


def solve(lines: list[str]) -> tuple[int, int]:
    lights = bytearray(1_000_000)
    brightness = [0] * 1_000_000
    for line in lines:
        match = COMMAND.fullmatch(line)
        if not match:
            continue
        command, *coords = match.groups()
        x1, y1, x2, y2 = map(int, coords)
        for y in range(y1, y2 + 1):
            start, end = y * 1000 + x1, y * 1000 + x2 + 1
            if command == 'toggle':
                for i in range(start, end):
                    lights[i] ^= 1
                    brightness[i] += 2
            elif command == 'turn on':
                lights[start:end] = b'\x01' * (end - start)
                for i in range(start, end):
                    brightness[i] += 1
            else:
                lights[start:end] = b'\x00' * (end - start)
                for i in range(start, end):
                    brightness[i] = max(0, brightness[i] - 1)
    return sum(lights), sum(brightness)


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
