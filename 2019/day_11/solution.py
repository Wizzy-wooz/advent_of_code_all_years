from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]));
from intcode import Computer


def paint(data, start=0):
    c = Computer(list(map(int, data.strip().split(","))));
    panels = {(0, 0): start};
    painted = set();
    x = y = direction = 0
    while not c.halted:
        c.inputs.append(panels.get((x, y), 0));
        out = c.run()
        if not out: break
        color, turn = out[-2:];
        panels[(x, y)] = color;
        painted.add((x, y));
        direction = (direction + (1 if turn else -1)) % 4
        dx, dy = ((0, -1), (1, 0), (0, 1), (-1, 0))[direction];
        x += dx;
        y += dy
    return painted, panels


def part1(data): return len(paint(data)[0])


def part2(data):
    _, p = paint(data, 1);
    xs = [x for x, y in p];
    ys = [y for x, y in p]
    return "\n".join("".join("#" if p.get((x, y), 0) else " " for x in range(min(xs), max(xs) + 1)).rstrip() for y in
                     range(min(ys), max(ys) + 1))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:\n" + part2(d))
