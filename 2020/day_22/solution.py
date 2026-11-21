from collections import deque
from pathlib import Path


def parse(d): a, b = d.strip().split("\n\n");return deque(map(int, a.splitlines()[1:])), deque(
    map(int, b.splitlines()[1:]))


def score(deck): return sum(i * c for i, c in enumerate(reversed(deck), 1))


def combat(a, b, recursive=False):
    seen = set()
    while a and b:
        state = (tuple(a), tuple(b))
        if recursive and state in seen: return 1, a
        seen.add(state);
        x, y = a.popleft(), b.popleft()
        if recursive and len(a) >= x and len(b) >= y:
            w, _ = combat(deque(list(a)[:x]), deque(list(b)[:y]), True)
        else:
            w = 1 if x > y else 2
        (a if w == 1 else b).extend((x, y) if w == 1 else (y, x))
    return (1, a) if a else (2, b)


def part1(d): _, deck = combat(*parse(d));return score(deck)


def part2(d): _, deck = combat(*parse(d), True);return score(deck)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
