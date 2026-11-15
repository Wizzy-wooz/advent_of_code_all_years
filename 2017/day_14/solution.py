from collections import deque
from functools import reduce
from pathlib import Path

SUFFIX = [17, 31, 73, 47, 23]

def knot_hash(text: str) -> list[int]:
    values = list(range(256))
    lengths = [*text.encode(), *SUFFIX]
    position = skip = 0
    for _ in range(64):
        for length in lengths:
            for offset in range(length // 2):
                a, b = (position + offset) % 256, (position + length - offset - 1) % 256
                values[a], values[b] = values[b], values[a]
            position = (position + length + skip) % 256
            skip += 1
    return [reduce(int.__xor__, values[i:i + 16]) for i in range(0, 256, 16)]

def disk(key: str) -> list[list[int]]:
    return [[(byte >> bit) & 1 for byte in knot_hash(f"{key}-{row}") for bit in range(7, -1, -1)] for row in range(128)]

def part1(data: str) -> int:
    return sum(map(sum, disk(data.strip())))

def part2(data: str) -> int:
    grid = disk(data.strip())
    seen: set[tuple[int, int]] = set()
    regions = 0
    for row in range(128):
        for col in range(128):
            if not grid[row][col] or (row, col) in seen:
                continue
            regions += 1
            seen.add((row, col))
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < 128 and 0 <= nc < 128 and grid[nr][nc] and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        queue.append((nr, nc))
    return regions

if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
