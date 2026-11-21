from collections import defaultdict
from pathlib import Path


def reactions(data):
    out = {}
    for line in data.splitlines():
        if line.strip():
            left, right = line.split(" => ");
            n, name = right.split();
            out[name] = (int(n), [(int(a), b) for part in left.split(", ") for a, b in [part.split()]])
    return out


def ore_needed(data, fuel=1):
    rx = reactions(data);
    need = defaultdict(int, {"FUEL": fuel});
    spare = defaultdict(int)
    while any(k != "ORE" and v > 0 for k, v in need.items()):
        name = next(k for k, v in need.items() if k != "ORE" and v > 0);
        amount = need[name];
        used = min(amount, spare[name]);
        amount -= used;
        need[name] = 0;
        spare[name] -= used
        if not amount: continue
        batch, inputs = rx[name];
        runs = (amount + batch - 1) // batch;
        spare[name] += runs * batch - amount
        for n, ingredient in inputs: need[ingredient] += n * runs
    return need["ORE"]


def part1(data): return ore_needed(data)


def part2(data):
    lo, hi = 1, 1
    while ore_needed(data, hi) <= 1_000_000_000_000: hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if ore_needed(data, mid) <= 1_000_000_000_000:
            lo = mid
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
