from heapq import heappop, heappush
from pathlib import Path


def solve(d, deep=False):
    rows = [r for r in d.splitlines() if any(c in "ABCD" for c in r)];
    rooms = [list(r[3:10:2]) for r in rows];
    if deep: rooms = [rooms[0], list("DCBA"), list("DBAC"), rooms[1]]
    depth = len(rooms);
    start = "".join("." * 11 + "".join(r[i] for r in rooms) for i in range(0)) if False else "".join(
        ["." * 11] + ["".join(row[i] for row in rooms) for i in range(4)])
    goals = [c * depth for c in "ABCD"];
    costs = {"A": 1, "B": 10, "C": 100, "D": 1000};
    doors = (2, 4, 6, 8);
    stops = (0, 1, 3, 5, 7, 9, 10)

    def moves(s):
        hall = s[:11];
        rs = [s[11 + i * depth:11 + (i + 1) * depth] for i in range(4)]
        for x, c in enumerate(hall):
            if c == ".": continue
            room = ord(c) - 65;
            door = doors[room];
            step = 1 if door > x else -1
            if all(hall[z] == "." for z in range(x + step, door + step, step)) and all(v in (".", c) for v in rs[room]):
                slot = max(i for i, v in enumerate(rs[room]) if v == ".");
                nr = [list(r) for r in rs];
                nr[room][slot] = c;
                nh = list(hall);
                nh[x] = ".";
                yield "".join(nh + sum(nr, [])), (abs(door - x) + slot + 1) * costs[c]
        for room, r in enumerate(rs):
            if all(c == "." for c in r) or all(c == "ABCD"[room] for c in r if c != "."): continue
            slot = next(i for i, c in enumerate(r) if c != ".");
            c = r[slot];
            x = doors[room]
            for dest in stops:
                step = 1 if dest > x else -1
                if all(hall[z] == "." for z in range(x + step, dest + step, step)):
                    nr = [list(q) for q in rs];
                    nr[room][slot] = ".";
                    nh = list(hall);
                    nh[dest] = c;
                    yield "".join(nh + sum(nr, [])), (abs(dest - x) + slot + 1) * costs[c]

    goal = "." * 11 + "".join(goals);
    q = [(0, start)];
    best = {start: 0}
    while q:
        cost, s = heappop(q)
        if s == goal: return cost
        if cost != best[s]: continue
        for n, w in moves(s):
            nc = cost + w
            if nc < best.get(n, 10 ** 30): best[n] = nc;heappush(q, (nc, nc and n or n))


def part1(d): return solve(d)


def part2(d): return solve(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
