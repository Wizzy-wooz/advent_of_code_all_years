from heapq import heappop, heappush
from pathlib import Path
import re


def parse(data: str):
    return [
        tuple(map(int, re.findall(r"-?\d+", line)))
        for line in data.splitlines()
        if line.strip()
    ]


def part1(data: str) -> int:
    bots = parse(data)
    strongest = max(bots, key=lambda b: b[3])
    return sum(sum(abs(b[i] - strongest[i]) for i in range(3)) <= strongest[3] for b in bots)


def part2(data: str) -> int:
    bots = parse(data)

    def distance_to_cube(x, y, z, size, point):
        total = 0
        for center, coordinate in zip((x, y, z), point):
            if coordinate < center:
                total += center - coordinate
            elif coordinate > center + size - 1:
                total += coordinate - (center + size - 1)
        return total

    minx = min(x - r for x, y, z, r in bots)
    maxx = max(x + r for x, y, z, r in bots)
    miny = min(y - r for x, y, z, r in bots)
    maxy = max(y + r for x, y, z, r in bots)
    minz = min(z - r for x, y, z, r in bots)
    maxz = max(z + r for x, y, z, r in bots)
    size = 1
    while size < max(maxx - minx + 1, maxy - miny + 1, maxz - minz + 1):
        size *= 2

    def coverage(x, y, z, s):
        return sum(distance_to_cube(x, y, z, s, (bx, by, bz)) <= radius for bx, by, bz, radius in bots)

    heap = []
    serial = 0
    origin_distance = distance_to_cube(minx, miny, minz, size, (0, 0, 0))
    heappush(
        heap,
        (
            -coverage(minx, miny, minz, size),
            origin_distance,
            size,
            serial,
            minx,
            miny,
            minz,
        ),
    )
    serial += 1
    while heap:
        neg_count, dist, size, _, x, y, z = heappop(heap)
        if size == 1:
            return dist

        half = size // 2
        for dx in (0, half):
            for dy in (0, half):
                for dz in (0, half):
                    nx, ny, nz = x + dx, y + dy, z + dz
                    count = coverage(nx, ny, nz, half)
                    if count:
                        distance = distance_to_cube(nx, ny, nz, half, (0, 0, 0))
                        heappush(
                            heap,
                            (-count, distance, half, serial, nx, ny, nz),
                        )
                        serial += 1
    raise ValueError("No point found")


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
