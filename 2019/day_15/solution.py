from collections import deque
from copy import deepcopy
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]));
from intcode import Computer

MOVES = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}


def explore(data):
    start = Computer(list(map(int, data.strip().split(","))));
    q = deque([((0, 0), start, 0)]);
    tiles = {(0, 0): 1};
    oxygen = None;
    distance = 0
    while q:
        (x, y), c, d = q.popleft()
        for cmd, (dx, dy) in MOVES.items():
            p = (x + dx, y + dy)
            if p in tiles: continue
            nxt = deepcopy(c);
            nxt.inputs.append(cmd);
            status = nxt.run()[-1];
            tiles[p] = status
            if status:
                q.append((p, nxt, d + 1))
                if status == 2: oxygen = p;distance = d + 1
    if oxygen is None: raise ValueError("Oxygen system not found")
    q = deque([(oxygen, 0)]);
    seen = {oxygen};
    fill = 0
    while q:
        p, d = q.popleft();
        fill = max(fill, d)
        for dx, dy in MOVES.values():
            n = (p[0] + dx, p[1] + dy)
            if tiles.get(n, 0) > 0 and n not in seen: seen.add(n);q.append((n, d + 1))
    return distance, fill


def part1(data): return explore(data)[0]


def part2(data): return explore(data)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
