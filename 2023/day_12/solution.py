from functools import lru_cache
from pathlib import Path


def count(pattern, groups):
    @lru_cache(None)
    def dp(i, j, run):
        if i == len(pattern): return int((j == len(groups) and run == 0) or (j == len(groups) - 1 and run == groups[j]))
        total = 0
        for c in (".#" if pattern[i] == "?" else pattern[i]):
            if c == "#":
                if j < len(groups) and run < groups[j]: total += dp(i + 1, j, run + 1)
            elif run == 0:
                total += dp(i + 1, j, 0)
            elif j < len(groups) and run == groups[j]:
                total += dp(i + 1, j + 1, 0)
        return total

    return dp(0, 0, 0)


def solve(d, repeat):
    return sum(
        count("?".join([a] * repeat), tuple(map(int, b.split(","))) * repeat) for line in d.splitlines() if line.strip()
        for a, b in [line.split()])


def part1(d): return solve(d, 1)


def part2(d): return solve(d, 5)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
