from pathlib import Path


def longest(d, slopes):
    g = d.splitlines();
    h = len(g);
    w = len(g[0]);
    start = (g[0].index("."), 0);
    end = (g[-1].index("."), h - 1);
    dirs = ((1, 0), (0, 1), (-1, 0), (0, -1));
    nodes = {start, end}
    for y in range(h):
        for x in range(w):
            if g[y][x] != "#" and sum(
                0 <= x + dx < w and 0 <= y + dy < h and g[y + dy][x + dx] != "#" for dx, dy in dirs) > 2: nodes.add(
                (x, y))
    graph = {p: [] for p in nodes}
    for p in nodes:
        q = [(p, 0, {p})]
        for pos, dist, seen in q:
            x, y = pos
            options = [(x + dx, y + dy) for dx, dy in dirs if
                       0 <= x + dx < w and 0 <= y + dy < h and g[y + dy][x + dx] != "#" and (x + dx,
                                                                                             y + dy) not in seen]
            if slopes and g[y][x] in ">v<^":
                dx, dy = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}[g[y][x]];
                options = [p2 for p2 in options if p2 == (x + dx, y + dy)]
            for nxt in options:
                if nxt in nodes:
                    graph[p].append((nxt, dist + 1))
                else:
                    q.append((nxt, dist + 1, seen | {nxt}))

    def dfs(p, seen):
        if p == end: return 0
        return max((n + dfs(q, seen | {q}) for q, n in graph[p] if q not in seen), default=-10 ** 9)

    return dfs(start, {start})


def part1(d): return longest(d, True)


def part2(d): return longest(d, False)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
