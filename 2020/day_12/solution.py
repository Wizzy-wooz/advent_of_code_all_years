from pathlib import Path


def navigate(d, waypoint=False):
    x = y = 0;
    wx, wy = (10, 1) if waypoint else (1, 0)
    for line in d.splitlines():
        if not line.strip(): continue
        op = line[0];
        n = int(line[1:])
        if op in "LR":
            for _ in range((n // 90) % 4 if op == "R" else (4 - n // 90) % 4): wx, wy = wy, -wx
        elif op == "F":
            x += wx * n;y += wy * n
        elif waypoint:
            if op == "N":
                wy += n
            elif op == "S":
                wy -= n
            elif op == "E":
                wx += n
            elif op == "W":
                wx -= n
        else:
            if op == "N":
                y += n
            elif op == "S":
                y -= n
            elif op == "E":
                x += n
            elif op == "W":
                x -= n
    return abs(x) + abs(y)


def part1(d): return navigate(d)


def part2(d): return navigate(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
