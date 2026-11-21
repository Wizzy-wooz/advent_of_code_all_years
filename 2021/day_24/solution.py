from pathlib import Path
import re


def solve(d):
    blocks = d.strip().split("inp w\n")[1:];
    stack = [];
    pairs = []
    for i, b in enumerate(blocks):
        vals = list(map(int, re.findall(r"(?:div z|add x|add y) (-?\d+)", b)))
        div, ax, ay = vals[0], vals[1], vals[-1]
        if div == 1:
            stack.append((i, ay))
        else:
            j, prev = stack.pop();pairs.append((j, i, prev + ax))

    def make(high):
        digits = [0] * len(blocks)
        for a, b, delta in pairs:
            for x in (range(9, 0, -1) if high else range(1, 10)):
                y = x + delta
                if 1 <= y <= 9: digits[a] = x;digits[b] = y;break
        return int("".join(map(str, digits)))

    return make(True), make(False)


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
