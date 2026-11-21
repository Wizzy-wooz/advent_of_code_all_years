from functools import lru_cache
from pathlib import Path
import re


def maximum(line, minutes):
    a = list(map(int, re.findall(r"\d+", line)));
    _, ore, clay, obore, obclay, geore, geobs = a
    costs = ((ore, 0, 0), (clay, 0, 0), (obore, obclay, 0), (geore, 0, geobs));
    maxcost = tuple(max(c[i] for c in costs) for i in range(3))

    @lru_cache(None)
    def dfs(t, ore, clay, obs, ro, rc, rb, rg):
        if t == 0: return 0
        best = rg * t
        for typ, cost in enumerate(costs):
            if typ < 3 and (ro, rc, rb)[typ] >= maxcost[typ]: continue
            waits = [];
            possible = True
            for need, have, rate in zip(cost, (ore, clay, obs), (ro, rc, rb)):
                if need > have:
                    if not rate: possible = False;break
                    waits.append((need - have + rate - 1) // rate)
            if not possible: continue
            dt = max(waits, default=0) + 1
            if dt >= t: continue
            state = (ore + ro * dt - cost[0], clay + rc * dt - cost[1], obs + rb * dt - cost[2], ro + (typ == 0),
                     rc + (typ == 1), rb + (typ == 2), rg + (typ == 3))
            best = max(best, rg * dt + dfs(t - dt, *state))
        return best

    return dfs(minutes, 0, 0, 0, 1, 0, 0, 0)


def part1(d): return sum(i * maximum(line, 24) for i, line in enumerate((x for x in d.splitlines() if x.strip()), 1))


def part2(d):
    from math import prod
    return prod(maximum(line, 32) for line in [x for x in d.splitlines() if x.strip()][:3])


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
