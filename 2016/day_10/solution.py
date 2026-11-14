import re
from collections import defaultdict, deque


def run(data: str, compare: tuple[int, int] = (17, 61)) -> tuple[int | None, int]:
    rules, bots, outputs = {}, defaultdict(list), defaultdict(list)
    for line in data.splitlines():
        if m := re.fullmatch(r'value (\d+) goes to bot (\d+)', line): bots[int(m[2])].append(int(m[1]))
        elif m := re.fullmatch(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', line):
            rules[int(m[1])] = ((m[2], int(m[3])), (m[4], int(m[5])))
    queue = deque(b for b, chips in bots.items() if len(chips) >= 2); comparer = None
    while queue:
        bot = queue.popleft()
        if len(bots[bot]) < 2: continue
        low, high = sorted(bots[bot]); bots[bot] = []
        if (low, high) == tuple(sorted(compare)): comparer = bot
        for value, (kind, dest) in zip((low, high), rules[bot]):
            if kind == 'output': outputs[dest].append(value)
            else:
                bots[dest].append(value)
                if len(bots[dest]) >= 2: queue.append(dest)
    product = outputs[0][0] * outputs[1][0] * outputs[2][0]
    return comparer, product


def part1(data: str) -> int | None: return run(data)[0]
def part2(data: str) -> int: return run(data)[1]


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
