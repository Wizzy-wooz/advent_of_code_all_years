from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]));
from intcode import Computer


def play(data, free=False):
    p = list(map(int, data.strip().split(",")));
    c = Computer(p)
    if free: c.mem[0] = 2
    screen = {};
    score = ball = paddle = 0
    while not c.halted:
        out = c.run()
        for i in range(0, len(out) - 2, 3):
            x, y, v = out[i:i + 3]
            if (x, y) == (-1, 0):
                score = v
            else:
                screen[x, y] = v
                if v == 3:
                    paddle = x
                elif v == 4:
                    ball = x
        if not c.halted: c.inputs.append((ball > paddle) - (ball < paddle))
    return score, screen


def part1(data): return sum(v == 2 for v in play(data)[1].values())


def part2(data): return play(data, True)[0]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
