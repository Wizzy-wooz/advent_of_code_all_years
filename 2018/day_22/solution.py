from functools import lru_cache
from heapq import heappop, heappush
from pathlib import Path
import re


def parse(data: str):
    values = list(map(int, re.findall(r"\d+", data)))
    return values[0], (values[1], values[2])


def cave(data: str):
    depth, target = parse(data)

    @lru_cache(None)
    def erosion(x, y):
        if (x, y) in ((0, 0), target):
            geo = 0
        elif y == 0:
            geo = x * 16807
        elif x == 0:
            geo = y * 48271
        else:
            geo = erosion(x - 1, y) * erosion(x, y - 1)
        return (geo + depth) % 20183

    return target, erosion


def part1(data: str) -> int:
    (tx, ty), erosion = cave(data)
    return sum(erosion(x, y) % 3 for y in range(ty + 1) for x in range(tx + 1))


def part2(data: str) -> int:
    target, erosion = cave(data)
    tx, ty = target
    torch, climbing_gear, neither = range(3)
    allowed = (
        (torch, climbing_gear),
        (climbing_gear, neither),
        (torch, neither),
    )
    start = (0, 0, torch)
    goal = (tx, ty, torch)
    queue = [(0, *start)]
    best = {start: 0}
    while queue:
        time, x, y, tool = heappop(queue)
        if time != best[(x, y, tool)]:
            continue
        if (x, y, tool) == goal:
            return time

        region = erosion(x, y) % 3
        for new_tool in allowed[region]:
            if new_tool != tool:
                state = (x, y, new_tool)
                candidate = time + 7
                if candidate < best.get(state, 10**30):
                    best[state] = candidate
                    heappush(queue, (candidate, *state))

        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if nx >= 0 and ny >= 0 and tool in allowed[erosion(nx, ny) % 3]:
                state = (nx, ny, tool)
                candidate = time + 1
                if candidate < best.get(state, 10**30):
                    best[state] = candidate
                    heappush(queue, (candidate, *state))
    raise ValueError("Target is unreachable")


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
