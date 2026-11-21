from pathlib import Path


def valid(n: int, exact: bool = False) -> bool:
    s = str(n)
    if any(a > b for a, b in zip(s, s[1:])): return False
    runs = [len(list(g)) for _, g in __import__("itertools").groupby(s)]
    return 2 in runs if exact else any(r >= 2 for r in runs)


def solve(data: str):
    lo, hi = map(int, data.strip().split("-"));
    return sum(valid(n) for n in range(lo, hi + 1)), sum(valid(n, True) for n in range(lo, hi + 1))


def part1(data: str) -> int: return solve(data)[0]


def part2(data: str) -> int: return solve(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
