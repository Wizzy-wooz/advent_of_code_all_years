from pathlib import Path
import re


def area(d, encoded):
    pts = [(0, 0)];
    border = 0
    for line in d.splitlines():
        if not line.strip(): continue
        direction, n, color = re.fullmatch(r"([RDLU]) (\d+) \(#([0-9a-f]+)\)", line).groups()
        if encoded: n = int(color[:5], 16);direction = "RDLU"[int(color[5])]
        dx, dy = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}[direction];
        x, y = pts[-1];
        pts.append((x + dx * int(n), y + dy * int(n)));
        border += int(n)
    return (abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(pts, pts[1:]))) + border) // 2 + 1


def part1(d): return area(d, False)


def part2(d): return area(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
