from pathlib import Path


def trace(line: str):
    x = y = steps = 0;
    seen = {}
    for part in line.split(","):
        dx, dy = ({"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}[part[0]]);
        n = int(part[1:])
        for _ in range(n):
            x += dx;
            y += dy;
            steps += 1;
            seen.setdefault((x, y), steps)
    return seen


def intersections(data: str):
    a, b = (trace(line) for line in data.splitlines() if line.strip());
    common = a.keys() & b.keys()
    if not common: raise ValueError("Wires do not intersect")
    return min(abs(x) + abs(y) for x, y in common), min(a[p] + b[p] for p in common)


def part1(data: str) -> int: return intersections(data)[0]


def part2(data: str) -> int: return intersections(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
