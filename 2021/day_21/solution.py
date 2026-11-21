from functools import lru_cache
from pathlib import Path


def parse(d): return [int(x.split(": ")[1]) for x in d.splitlines() if x.strip()]


def part1(d):
    p = parse(d);
    s = [0, 0];
    die = roll = turn = 0
    while max(s) < 1000:
        n = 0
        for _ in range(3): die = die % 100 + 1;n += die;roll += 1
        p[turn] = (p[turn] + n - 1) % 10 + 1;
        s[turn] += p[turn];
        turn ^= 1
    return min(s) * roll


def part2(d):
    p = parse(d);
    freq = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

    @lru_cache(None)
    def play(a, b, sa, sb, t):
        wins = [0, 0]
        for r, n in freq.items():
            if t == 0:
                na = (a + r - 1) % 10 + 1;
                ns = sa + na
                if ns >= 21:
                    wins[0] += n
                else:
                    x, y = play(na, b, ns, sb, 1);wins[0] += n * x;wins[1] += n * y
            else:
                nb = (b + r - 1) % 10 + 1;
                ns = sb + nb
                if ns >= 21:
                    wins[1] += n
                else:
                    x, y = play(a, nb, sa, ns, 0);wins[0] += n * x;wins[1] += n * y
        return tuple(wins)

    return max(play(*p, 0, 0, 0))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
