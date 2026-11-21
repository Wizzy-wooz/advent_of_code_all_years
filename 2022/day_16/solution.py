from functools import lru_cache
from pathlib import Path
import re


def solve(d):
    flow = {};
    edges = {}
    for line in d.splitlines():
        if line.strip():
            name = line[6:8];
            flow[name] = int(re.search(r"rate=(\d+)", line).group(1));
            edges[name] = re.findall(r"[A-Z]{2}", line.split("valve")[-1])
    useful = [x for x in flow if flow[x]];
    dist = {}
    for s in ["AA"] + useful:
        q = [(s, 0)];
        seen = {s}
        for n, k in q:
            dist[s, n] = k
            for v in edges[n]:
                if v not in seen: seen.add(v);q.append((v, k + 1))

    @lru_cache(None)
    def best(pos, time, mask):
        ans = 0
        for i, v in enumerate(useful):
            if mask >> i & 1: continue
            rem = time - dist[pos, v] - 1
            if rem > 0: ans = max(ans, flow[v] * rem + best(v, rem, mask | 1 << i))
        return ans

    one = best("AA", 30, 0);
    n = len(useful);
    two = max(best("AA", 26, m) + best("AA", 26, ((1 << n) - 1) ^ m) for m in range(1 << n))
    return one, two


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
