from collections import defaultdict
from pathlib import Path

def simulate(data: str, bursts: int, evolved: bool) -> int:
    rows = data.splitlines()
    grid = {(x - len(rows[0]) // 2, y - len(rows) // 2): "#" for y, row in enumerate(rows) for x, char in enumerate(row) if char == "#"}
    x = y = direction = infections = 0
    deltas = ((0, -1), (1, 0), (0, 1), (-1, 0))
    for _ in range(bursts):
        state = grid.get((x, y), ".")
        if evolved:
            if state == ".": direction = (direction - 1) % 4; grid[(x, y)] = "W"
            elif state == "W": grid[(x, y)] = "#"; infections += 1
            elif state == "#": direction = (direction + 1) % 4; grid[(x, y)] = "F"
            else: direction = (direction + 2) % 4; grid.pop((x, y), None)
        elif state == "#": direction = (direction + 1) % 4; grid.pop((x, y))
        else: direction = (direction - 1) % 4; grid[(x, y)] = "#"; infections += 1
        dx, dy = deltas[direction]
        x += dx; y += dy
    return infections

def part1(data: str) -> int: return simulate(data, 10_000, False)
def part2(data: str) -> int: return simulate(data, 10_000_000, True)

if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
