from pathlib import Path
import re


def reboot(d, limit=None):
    cubes = []
    for line in d.splitlines():
        if not line.strip(): continue
        on, *nums = line.split();
        x1, x2, y1, y2, z1, z2 = map(int, re.findall(r"-?\d+", line));
        box = (x1, x2, y1, y2, z1, z2)
        if limit is not None:
            x1, x2, y1, y2, z1, z2 = box;
            x1 = max(x1, -limit);
            x2 = min(x2, limit);
            y1 = max(y1, -limit);
            y2 = min(y2, limit);
            z1 = max(z1, -limit);
            z2 = min(z2, limit);
            box = (x1, x2, y1, y2, z1, z2)
        if box[0] > box[1] or box[2] > box[3] or box[4] > box[5]: continue
        adds = []
        for old, sign in cubes:
            ix1 = max(box[0], old[0]);
            ix2 = min(box[1], old[1]);
            iy1 = max(box[2], old[2]);
            iy2 = min(box[3], old[3]);
            iz1 = max(box[4], old[4]);
            iz2 = min(box[5], old[5])
            if ix1 <= ix2 and iy1 <= iy2 and iz1 <= iz2: adds.append(((ix1, ix2, iy1, iy2, iz1, iz2), -sign))
        if on == "on": adds.append((box, 1))
        cubes += adds
    return sum(s * (b - a + 1) * (d - c + 1) * (f - e + 1) for (a, b, c, d, e, f), s in cubes)


def part1(d): return reboot(d, 50)


def part2(d): return reboot(d)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
