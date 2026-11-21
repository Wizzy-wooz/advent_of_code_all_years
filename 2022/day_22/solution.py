from math import gcd
from pathlib import Path
import re


def parse(data):
    board, path = data.rstrip().split("\n\n")
    return board.splitlines(), [(int(n), turn) for n, turn in re.findall(r"(\d+)([LR]?)", path)]


def planar(rows, path):
    grid = [row.ljust(max(map(len, rows))) for row in rows]
    x, y, facing = grid[0].index("."), 0, 0
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for count, turn in path:
        for _ in range(count):
            dx, dy = directions[facing]
            nx, ny = (x + dx) % len(grid[0]), (y + dy) % len(grid)
            while grid[ny][nx] == " ":
                nx, ny = (nx + dx) % len(grid[0]), (ny + dy) % len(grid)
            if grid[ny][nx] == "#":
                break
            x, y = nx, ny
        if turn:
            facing = (facing + (1 if turn == "R" else -1)) % 4
    return 1000 * (y + 1) + 4 * (x + 1) + facing


def cube(rows, path):
    grid = [row.ljust(max(map(len, rows))) for row in rows]
    size = 0
    for row in grid:
        for run in re.findall(r"[^ ]+", row):
            size = gcd(size, len(run))
    faces = {(x // size, y // size) for y, row in enumerate(grid) for x, char in enumerate(row) if char != " "}
    start = min(faces, key=lambda p: (p[1], p[0]))
    neg = lambda a: tuple(-v for v in a)
    orientations = {start: ((1, 0, 0), (0, 1, 0), (0, 0, 1))}
    todo = [start]
    while todo:
        fx, fy = todo.pop()
        u, v, normal = orientations[(fx, fy)]
        adjacent = ((1, 0, (neg(normal), v, u)), (-1, 0, (normal, v, neg(u))),
                    (0, 1, (u, neg(normal), v)), (0, -1, (u, normal, neg(v))))
        for dx, dy, orientation in adjacent:
            face = (fx + dx, fy + dy)
            if face in faces and face not in orientations:
                orientations[face] = orientation
                todo.append(face)
    normal_face = {orientation[2]: face for face, orientation in orientations.items()}
    face = start
    x = grid[face[1] * size].index(".")
    y = face[1] * size
    facing = 0  # east, south, west, north
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for count, turn in path:
        for _ in range(count):
            fx, fy = x // size, y // size
            u, v, normal = orientations[(fx, fy)]
            lx, ly = x % size, y % size
            dx, dy = directions[facing]
            nx, ny, next_facing = x + dx, y + dy, facing
            if (nx // size, ny // size) not in faces:
                target_normal = (u, v, neg(u), neg(v))[facing]
                tx, ty = normal_face[target_normal]
                tu, tv, _ = orientations[(tx, ty)]
                next_facing = next(i for i, vec in enumerate((tu, tv, neg(tu), neg(tv))) if vec == neg(normal))
                offset = ly if facing in (0, 2) else lx
                old_axis = v if facing in (0, 2) else u
                new_axis = tv if next_facing in (0, 2) else tu
                if old_axis == neg(new_axis):
                    offset = size - 1 - offset
                elif old_axis != new_axis:
                    raise ValueError("Cube edge orientations do not align")
                if next_facing == 0:
                    nx, ny = tx * size, ty * size + offset
                elif next_facing == 1:
                    nx, ny = tx * size + offset, ty * size
                elif next_facing == 2:
                    nx, ny = tx * size + size - 1, ty * size + offset
                else:
                    nx, ny = tx * size + offset, ty * size + size - 1
            if grid[ny][nx] == "#":
                break
            x, y, facing = nx, ny, next_facing
        if turn:
            facing = (facing + (1 if turn == "R" else -1)) % 4
    return 1000 * (y + 1) + 4 * (x + 1) + facing


def part1(data):
    rows, path = parse(data)
    return planar(rows, path)


def part2(data):
    rows, path = parse(data)
    return cube(rows, path)


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
