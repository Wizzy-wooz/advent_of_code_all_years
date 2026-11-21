from functools import lru_cache
from pathlib import Path


@lru_cache(None)
def count(n, steps):
    if not steps: return 1
    if n == 0: return count(1, steps - 1)
    s = str(n)
    if len(s) % 2 == 0: return count(int(s[:len(s) // 2]), steps - 1) + count(int(s[len(s) // 2:]), steps - 1)
    return count(n * 2024, steps - 1)


def solve(d, n): return sum(count(int(x), n) for x in d.split())


def part1(d): return solve(d, 25)


def part2(d): return solve(d, 75)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
