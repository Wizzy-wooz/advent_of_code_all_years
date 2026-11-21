from collections import deque
from functools import cache
from math import inf
from pathlib import Path


def solve(data, split=False):
    g = [list(r) for r in data.splitlines()];
    starts = [(x, y) for y, r in enumerate(g) for x, c in enumerate(r) if c == "@"]
    if split:
        x, y = starts[0]
        for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)): g[y + dy][x + dx] = "#"
        starts = [(x + dx, y + dy) for dx, dy in ((-1, -1), (1, -1), (-1, 1), (1, 1))]
        for x, y in starts: g[y][x] = "@"
    goal = sum(1 << (ord(c) - 97) for row in g for c in row if c.islower())

    @cache
    def reachable(start, mask):
        queue = deque([(start, 0)])
        visited = {start}
        keys = []
        while queue:
            (x, y), distance = queue.popleft()
            for position in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if position in visited:
                    continue
                visited.add(position)
                nx, ny = position
                tile = g[ny][nx]
                if tile == "#":
                    continue
                if tile.isalpha():
                    bit = 1 << (ord(tile.lower()) - 97)
                    if not mask & bit:
                        if tile.islower():
                            keys.append((position, bit, distance + 1))
                        continue
                queue.append((position, distance + 1))
        return keys

    @cache
    def remaining(positions, mask):
        if mask == goal:
            return 0
        best = inf
        for i, start in enumerate(positions):
            for key, bit, distance in reachable(start, mask):
                moved = positions[:i] + (key,) + positions[i + 1:]
                best = min(best, distance + remaining(moved, mask | bit))
        return best

    answer = remaining(tuple(starts), 0)
    if answer == inf:
        raise ValueError("Not all keys are reachable")
    return answer


def part1(data): return solve(data)


def part2(data): return solve(data, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
