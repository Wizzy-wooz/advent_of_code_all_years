from fractions import Fraction
from itertools import combinations
from pathlib import Path
import re


def parse(d): return [tuple(map(int, re.findall(r"-?\d+", x))) for x in d.splitlines() if x.strip()]


def part1(d, lo=200000000000000, hi=400000000000000):
    a = parse(d);
    count = 0
    for p, q in combinations(a, 2):
        x, y, vx, vy = p[:4];
        X, Y, VX, VY = q[:4];
        det = vx * VY - vy * VX
        if not det: continue
        t = Fraction((X - x) * VY - (Y - y) * VX, det);
        u = Fraction((X - x) * vy - (Y - y) * vx, det)
        if t >= 0 and u >= 0 and lo <= x + vx * t <= hi and lo <= y + vy * t <= hi: count += 1
    return count


def part2(d):
    h = parse(d)[:3];
    rows = []
    # Linearized cross-product equations for rock position and velocity.
    for (x, y, z, vx, vy, vz), (X, Y, Z, VX, VY, VZ) in zip(h, h[1:]):
        rows += [[0, vz - VZ, VY - vy, 0, Z - z, y - Y, (y * vz - z * vy) - (Y * VZ - Z * VY)],
                 [vz * -1 + VZ, 0, vx - VX, Z * -1 + z, 0, x - X, (z * vy - x * vz) - (Z * VY - X * VZ)],
                 [vy - VY, VX - vx, 0, Y - y, x - X, 0, (x * vy - y * vx) - (X * VY - Y * VX)]]
    m = [[Fraction(v) for v in r] for r in rows]
    for c in range(6):
        pivot = next(i for i in range(c, len(m)) if m[i][c]);
        m[c], m[pivot] = m[pivot], m[c];
        factor = m[c][c];
        m[c] = [x / factor for x in m[c]]
        for i in range(len(m)):
            if i != c:
                factor = m[i][c];
                m[i] = [a - factor * b for a, b in zip(m[i], m[c])]
    return int(sum(m[i][-1] for i in range(3)))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
