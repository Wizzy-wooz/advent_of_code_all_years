from pathlib import Path

CONNECTIONS = {
    "|": {(0, -1), (0, 1)}, "-": {(-1, 0), (1, 0)},
    "L": {(0, -1), (1, 0)}, "J": {(0, -1), (-1, 0)},
    "7": {(0, 1), (-1, 0)}, "F": {(0, 1), (1, 0)},
}


def solve(data: str) -> tuple[int, int]:
    grid = data.splitlines()
    height, width = len(grid), len(grid[0])
    start = next((x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == "S")
    sx, sy = start
    start_directions = {
        (dx, dy) for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0))
        if 0 <= sx + dx < width and 0 <= sy + dy < height
           and (-dx, -dy) in CONNECTIONS.get(grid[sy + dy][sx + dx], set())
    }
    path = [start]
    previous = start
    dx, dy = next(iter(start_directions))
    current = (sx + dx, sy + dy)
    while current != start:
        path.append(current)
        x, y = current
        options = CONNECTIONS[grid[y][x]]
        nxt = next((x + ox, y + oy) for ox, oy in options if (x + ox, y + oy) != previous)
        previous, current = current, nxt

    doubled_area = abs(sum(
        x1 * y2 - x2 * y1
        for (x1, y1), (x2, y2) in zip(path, path[1:] + path[:1])
    ))
    boundary = len(path)
    return boundary // 2, (doubled_area - boundary) // 2 + 1


def part1(data: str) -> int:
    return solve(data)[0]


def part2(data: str) -> int:
    return solve(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
