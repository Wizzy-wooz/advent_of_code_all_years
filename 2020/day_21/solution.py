from pathlib import Path
import re


def solve(d):
    foods = [];
    possible = {}
    for line in d.splitlines():
        if not line.strip(): continue
        ingredients, allergens = line.split(" (contains ");
        items = set(ingredients.split());
        foods.append(items)
        for a in allergens[:-1].split(", "): possible[a] = possible[a] & items if a in possible else items.copy()
    bad = set.union(*possible.values());
    safe = sum(len(items - bad) for items in foods);
    mapping = {}
    while len(mapping) < len(possible):
        a = next(k for k, v in possible.items() if k not in mapping and len(v) == 1);
        i = next(iter(possible[a]));
        mapping[a] = i
        for k in possible:
            if k != a: possible[k].discard(i)
    return safe, ",".join(mapping[a] for a in sorted(mapping))


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
