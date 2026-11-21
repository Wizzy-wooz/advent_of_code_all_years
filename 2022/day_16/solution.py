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

    count = len(useful)
    size = 1 << count

    def scores(minutes):
        result = [0] * size
        seen = {}

        def visit(position, time, opened, score):
            state = (position, time, opened)
            if seen.get(state, -1) >= score:
                return
            seen[state] = score
            result[opened] = max(result[opened], score)
            for i, valve in enumerate(useful):
                bit = 1 << i
                remaining = time - dist[position, valve] - 1
                if remaining > 0 and not opened & bit:
                    visit(valve, remaining, opened | bit, score + flow[valve] * remaining)

        visit("AA", minutes, 0, 0)
        return result

    one = max(scores(30))
    two_actor_scores = scores(26)
    # For each allowed set, either use its current best or leave out a valve.
    for i in range(count):
        bit = 1 << i
        for mask in range(size):
            if mask & bit:
                two_actor_scores[mask] = max(two_actor_scores[mask], two_actor_scores[mask ^ bit])
    two = max(score + two_actor_scores[size - 1 - mask] for mask, score in enumerate(two_actor_scores))
    return one, two


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    one, two = solve(d)
    print("Part 1:", one)
    print("Part 2:", two)
