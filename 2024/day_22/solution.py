from collections import defaultdict
from pathlib import Path


def nxt(n):
    n = (n ^ (n * 64)) % 16777216;
    n = (n ^ (n // 32)) % 16777216;
    return (n ^ (n * 2048)) % 16777216


def solve(d):
    nums = list(map(int, d.split()));
    total = 0;
    bananas = defaultdict(int)
    for n in nums:
        prices = [n % 10];
        x = n
        for _ in range(2000): x = nxt(x);prices.append(x % 10)
        total += x;
        seen = set()
        for i in range(4, len(prices)):
            key = tuple(prices[j] - prices[j - 1] for j in range(i - 3, i + 1))
            if key not in seen: bananas[key] += prices[i];seen.add(key)
    return total, max(bananas.values())


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
