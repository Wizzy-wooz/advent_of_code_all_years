from pathlib import Path
import re


def sensors(d):
    for line in d.splitlines():
        if line.strip(): sx, sy, bx, by = map(int, re.findall(r"-?\d+", line));yield sx, sy, bx, by, abs(sx - bx) + abs(
            sy - by)


def intervals(d, y):
    out = []
    for x, sy, bx, by, r in sensors(d):
        rem = r - abs(sy - y)
        if rem >= 0: out.append((x - rem, x + rem))
    return sorted(out)


def part1(d, row=2_000_000):
    iv = intervals(d, row);
    n = 0;
    end = None
    for a, b in iv:
        if end is None:
            n += b - a + 1;end = b
        elif b > end:
            n += b - max(end + 1, a) + 1;end = b
    beacons = {(bx, by) for sx, sy, bx, by, r in sensors(d) if by == row and any(a <= bx <= b for a, b in iv)}
    return n - len(beacons)


def part2(d, bound=4_000_000):
    ss = list(sensors(d))
    for y in range(bound + 1):
        iv = intervals(d, y);
        x = 0
        for a, b in iv:
            if a > x: return x * 4_000_000 + y
            x = max(x, b + 1)
            if x > bound: break
        if x <= bound: return x * 4_000_000 + y
    raise ValueError("No uncovered position")


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
