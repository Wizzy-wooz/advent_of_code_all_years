from functools import cache
from itertools import combinations
from pathlib import Path


def parse(data: str) -> list[tuple[int, int]]:
    return [tuple(map(int, line.split(","))) for line in data.splitlines() if line.strip()]


def inside_or_on(point: tuple[int, int], polygon: list[tuple[int, int]]) -> bool:
    x, y = point
    inside = False
    for (ax, ay), (bx, by) in zip(polygon, polygon[1:] + polygon[:1]):
        # Boundary points count as part of the red/green region.
        if min(ax, bx) <= x <= max(ax, bx) and min(ay, by) <= y <= max(ay, by):
            if (bx - ax) * (y - ay) == (by - ay) * (x - ax):
                return True
        # The half-open vertical-edge test avoids counting vertices twice.
        if ax == bx and min(ay, by) <= y < max(ay, by) and ax > x:
            inside = not inside
    return inside


def rectangle_is_inside(
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        polygon: list[tuple[int, int]],
        contains,
) -> bool:
    corners = ((x1, y1), (x1, y2), (x2, y1), (x2, y2))
    if not all(contains(corner) for corner in corners):
        return False

    # Degenerate rectangles are line segments; check every tile on the segment.
    if x1 == x2:
        return all(contains((x1, y)) for y in range(y1, y2 + 1))
    if y1 == y2:
        return all(contains((x, y1)) for x in range(x1, x2 + 1))

    for (ax, ay), (bx, by) in zip(polygon, polygon[1:] + polygon[:1]):
        if ay == by:
            # A horizontal polygon edge enters the rectangle's open interior.
            if y1 < ay < y2 and max(x1, min(ax, bx)) < min(x2, max(ax, bx)):
                return False
        else:
            # A vertical polygon edge enters the rectangle's open interior.
            if x1 < ax < x2 and max(y1, min(ay, by)) < min(y2, max(ay, by)):
                return False
    return True


def solve(data: str) -> tuple[int, int]:
    points = parse(data)
    pairs = []
    for (ax, ay), (bx, by) in combinations(points, 2):
        x1, x2 = sorted((ax, bx))
        y1, y2 = sorted((ay, by))
        pairs.append(((x2 - x1 + 1) * (y2 - y1 + 1), x1, y1, x2, y2))

    largest_unrestricted = max((candidate[0] for candidate in pairs), default=0)

    @cache
    def contains(point: tuple[int, int]) -> bool:
        return inside_or_on(point, points)

    largest_valid = 0
    for area, x1, y1, x2, y2 in sorted(pairs, reverse=True):
        if area <= largest_valid:
            break
        if rectangle_is_inside(x1, y1, x2, y2, points, contains):
            largest_valid = area
            break
    return largest_unrestricted, largest_valid


def part1(data: str) -> int:
    return solve(data)[0]


def part2(data: str) -> int:
    return solve(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
