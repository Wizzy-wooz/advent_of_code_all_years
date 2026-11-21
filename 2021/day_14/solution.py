from collections import Counter
from pathlib import Path


def score(d, steps):
    a, b = d.strip().split("\n\n");
    rules = dict(line.split(" -> ") for line in b.splitlines());
    pairs = Counter(a[i:i + 2] for i in range(len(a) - 1));
    chars = Counter(a)
    for _ in range(steps):
        nxt = Counter()
        for pair, n in pairs.items():
            c = rules[pair];
            nxt[pair[0] + c] += n;
            nxt[c + pair[1]] += n;
            chars[c] += n
        pairs = nxt
    return max(chars.values()) - min(chars.values())


def part1(d): return score(d, 10)


def part2(d): return score(d, 40)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
