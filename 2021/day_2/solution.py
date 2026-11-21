from pathlib import Path


def solve(d):
    h = depth = aim = depth2 = 0
    for line in d.splitlines():
        if not line.strip(): continue
        op, n = line.split();
        n = int(n)
        if op == "forward":
            h += n;depth2 += aim * n
        elif op == "down":
            depth += n;aim += n
        else:
            depth -= n;aim -= n
    return h * depth, h * depth2


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
