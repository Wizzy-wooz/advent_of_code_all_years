from pathlib import Path


def simulate(d, n):
    rope = [[0, 0] for _ in range(n)];
    visited = {(0, 0)};
    delta = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    for line in d.splitlines():
        if not line.strip(): continue
        op, count = line.split();
        dx, dy = delta[op]
        for _ in range(int(count)):
            rope[0][0] += dx;
            rope[0][1] += dy
            for i in range(1, n):
                a, b = rope[i - 1][0] - rope[i][0], rope[i - 1][1] - rope[i][1]
                if max(abs(a), abs(b)) > 1: rope[i][0] += (a > 0) - (a < 0);rope[i][1] += (b > 0) - (b < 0)
            visited.add(tuple(rope[-1]))
    return len(visited)


def part1(d): return simulate(d, 2)


def part2(d): return simulate(d, 10)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
