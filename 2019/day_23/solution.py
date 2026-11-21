from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]));
from intcode import Computer


def network(data):
    p = list(map(int, data.strip().split(",")));
    nodes = [Computer(p, [i]) for i in range(50)];
    queues = [[] for _ in nodes];
    nat = None;
    first = None;
    last = None
    while True:
        idle = True
        for i, c in enumerate(nodes):
            c.inputs.extend(queues[i]);
            queues[i].clear()
            if not c.inputs:
                c.inputs.append(-1)
            else:
                idle = False
            out = c.run()
            if out: idle = False
            for j in range(0, len(out) - 2, 3):
                dest, x, y = out[j:j + 3]
                if dest == 255:
                    if first is None: first = y
                    nat = (x, y)
                else:
                    queues[dest].extend((x, y))
        if idle and all(not q and not c.inputs for q, c in zip(queues, nodes)) and nat:
            x, y = nat;
            queues[0].extend((x, y))
            if y == last: return first, y
            last = y


def part1(data): return network(data)[0]


def part2(data): return network(data)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
