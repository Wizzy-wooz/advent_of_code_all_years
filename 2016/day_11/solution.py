import re
from collections import deque


def minimum_moves(data: str) -> int:
    floors = []
    for line in data.lower().splitlines():
        items = []
        for element, kind in re.findall(r'([a-z]+)(?:-compatible)? (microchip|generator)', line):
            items.append((element, kind[0]))
        floors.append(items)
    elements = sorted({e for floor in floors for e, _ in floor})
    pairs = tuple(sorted((next(i for i, f in enumerate(floors) if (e, 'g') in f), next(i for i, f in enumerate(floors) if (e, 'm') in f)) for e in elements))
    start = (0, pairs); goal_floor = len(floors) - 1
    def safe(ps):
        gens = {g for g, _ in ps}
        return all(m == g or m not in gens for g, m in ps)
    q = deque([(start, 0)]); seen = {start}
    while q:
        (elev, ps), steps = q.popleft()
        if all(g == goal_floor and m == goal_floor for g, m in ps): return steps
        items = [(i, 0) for i, (g, _) in enumerate(ps) if g == elev] + [(i, 1) for i, (_, m) in enumerate(ps) if m == elev]
        for dest in (elev + 1, elev - 1):
            if not 0 <= dest < len(floors): continue
            for count in (1, 2):
                from itertools import combinations
                for cargo in combinations(items, count):
                    nxt = [list(pair) for pair in ps]
                    for i, kind in cargo: nxt[i][kind] = dest
                    nxt = tuple(sorted(map(tuple, nxt)))
                    state = (dest, nxt)
                    if state not in seen and safe(nxt): seen.add(state); q.append((state, steps + 1))
    raise ValueError('No solution')


def part1(data: str) -> int: return minimum_moves(data)
def part2(data: str) -> int:
    lines = data.splitlines()
    lines[0] += ' An elerium generator, an elerium-compatible microchip, a dilithium generator, and a dilithium-compatible microchip.'
    return minimum_moves('\n'.join(lines))


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
