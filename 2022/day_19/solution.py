from pathlib import Path
import re


def maximum(line, minutes):
    a = list(map(int, re.findall(r"\d+", line)));
    _, ore, clay, obore, obclay, geore, geobs = a
    costs = ((ore, 0, 0), (clay, 0, 0), (obore, obclay, 0), (geore, 0, geobs));
    maxcost = tuple(max(c[i] for c in costs) for i in range(3))

    best = 0
    seen = {}

    def search(time, resources, robots, geodes):
        nonlocal best
        best = max(best, geodes)
        # Even building a geode robot every remaining minute cannot beat best.
        if geodes + time * (time - 1) // 2 <= best:
            return
        resources = tuple(
            min(stock, cap * time - rate * (time - 1))
            for stock, cap, rate in zip(resources, maxcost, robots)
        )
        state = time, resources, robots
        if seen.get(state, -1) >= geodes:
            return
        seen[state] = geodes

        for kind in (3, 2, 1, 0):
            if kind < 3 and robots[kind] >= maxcost[kind]:
                continue
            cost = costs[kind]
            wait = 0
            for need, stock, rate in zip(cost, resources, robots):
                if need > stock:
                    if rate == 0:
                        break
                    wait = max(wait, (need - stock + rate - 1) // rate)
            else:
                elapsed = wait + 1
                remaining = time - elapsed
                if remaining <= 0:
                    continue
                stock = tuple(
                    have + rate * elapsed - need
                    for have, rate, need in zip(resources, robots, cost)
                )
                rates = tuple(rate + (index == kind) for index, rate in enumerate(robots))
                search(remaining, stock, rates, geodes + (remaining if kind == 3 else 0))

    search(minutes, (0, 0, 0), (1, 0, 0), 0)
    return best


def part1(d): return sum(i * maximum(line, 24) for i, line in enumerate((x for x in d.splitlines() if x.strip()), 1))


def part2(d):
    from math import prod
    return prod(maximum(line, 32) for line in [x for x in d.splitlines() if x.strip()][:3])


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
