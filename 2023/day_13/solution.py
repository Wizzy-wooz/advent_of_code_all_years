from pathlib import Path


def score(g, smudges):
    for i in range(1, len(g)):
        pairs = zip(g[i - 1::-1], g[i:]);
        diff = sum(a != b for x, y in pairs for a, b in zip(x, y))
        if diff == smudges: return 100 * i
    for i in range(1, len(g[0])):
        diff = sum(g[y][x] != g[y][2 * i - 1 - x] for y in range(len(g)) for x in range(max(0, 2 * i - len(g[y])), i))
        # Compare mirrored columns only where both sides exist.
        diff = sum(g[y][i - 1 - k] != g[y][i + k] for y in range(len(g)) for k in range(min(i, len(g[0]) - i)))
        if diff == smudges: return i
    return 0


def solve(d, n): return sum(score(b.splitlines(), n) for b in d.strip().split("\n\n"))


def part1(d): return solve(d, 0)


def part2(d): return solve(d, 1)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
