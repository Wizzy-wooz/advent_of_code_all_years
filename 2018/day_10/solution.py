from pathlib import Path
import re


def parse(data: str): return [tuple(map(int, re.findall(r"-?\d+", line))) for line in data.splitlines() if line.strip()]


def constellation(data: str) -> tuple[str, int]:
    points = parse(data)

    def bounds(t):
        xs = [x + vx * t for x, _, vx, _ in points];
        ys = [y + vy * t for _, y, _, vy in points]
        return (max(xs) - min(xs)) * (max(ys) - min(ys)), xs, ys

    # The compact message occurs near the minimum bounding area.
    t = 0;
    best_t = 0;
    best = float("inf")
    for candidate in range(200_000):
        area, _, _ = bounds(candidate)
        if area < best:
            best, best_t = area, candidate
        elif candidate > best_t + 100 and area > best:
            break
    _, xs, ys = bounds(best_t)
    minx, miny = min(xs), min(ys)
    pixels = {(x - minx, y - miny) for x, y in zip(xs, ys)}
    width, height = max(x for x, _ in pixels) + 1, max(y for _, y in pixels) + 1
    picture = "\n".join("".join("#" if (x, y) in pixels else " " for x in range(width)).rstrip() for y in range(height))
    return picture, best_t


def part1(data: str) -> str: return constellation(data)[0]


def part2(data: str) -> int: return constellation(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:\n" + part1(data));
    print("Part 2:", part2(data))
