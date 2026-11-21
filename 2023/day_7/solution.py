from collections import Counter
from pathlib import Path


def kind(hand, jokers):
    c = Counter(hand);
    j = c.pop("J", 0) if jokers else 0;
    counts = sorted(c.values(), reverse=True) or [0];
    counts[0] += j
    return {(5,): 6, (4, 1): 5, (3, 2): 4, (3, 1, 1): 3, (2, 2, 1): 2, (2, 1, 1, 1): 1, (1, 1, 1, 1, 1): 0}.get(
        tuple(counts), 0)


def score(d, j=False):
    order = "J23456789TQKA" if j else "23456789TJQKA";
    hands = []
    for line in d.splitlines():
        if line.strip(): h, b = line.split();hands.append((kind(h, j), tuple(order.index(c) for c in h), int(b)))
    return sum(i * b for i, (_, _, b) in enumerate(sorted(hands), 1))


def part1(d): return score(d)


def part2(d): return score(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
