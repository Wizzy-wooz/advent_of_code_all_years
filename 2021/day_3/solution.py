from collections import Counter
from pathlib import Path


def solve(d):
    rows = [x.strip() for x in d.splitlines() if x.strip()];
    gamma = int("".join(Counter(c for c in col).most_common(1)[0][0] for col in zip(*rows)), 2);
    eps = (1 << len(rows[0])) - 1 - gamma

    def rating(most):
        items = rows[:]
        for i in range(len(rows[0])):
            c = Counter(x[i] for x in items);
            bit = ("1" if c["1"] >= c["0"] else "0") if most else ("0" if c["0"] <= c["1"] else "1")
            items = [x for x in items if x[i] == bit]
            if len(items) == 1: return int(items[0], 2)

    return gamma * eps, rating(True) * rating(False)


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
