from itertools import permutations
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]));
from intcode import Computer


def serial(data, phases):
    p = list(map(int, data.strip().split(",")));
    signal = 0
    for phase in phases: signal = Computer(p, [phase, signal]).run()[-1]
    return signal


def feedback(data, phases):
    p = list(map(int, data.strip().split(",")));
    cs = [Computer(p, [phase]) for phase in phases];
    cs[0].inputs.append(0);
    last = 0
    while not all(c.halted for c in cs):
        for i, c in enumerate(cs):
            out = c.run()
            if out:
                cs[(i + 1) % 5].inputs.extend(out)
                if i == 4: last = out[-1]
    return last


def part1(data): return max(serial(data, p) for p in permutations(range(5)))


def part2(data): return max(feedback(data, p) for p in permutations(range(5, 10)))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
