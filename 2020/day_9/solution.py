from itertools import combinations
from pathlib import Path


def invalid(nums, preamble):
    for i in range(preamble, len(nums)):
        if not any(a + b == nums[i] for a, b in combinations(nums[i - preamble:i], 2)): return nums[i], i
    raise ValueError("All values are valid")


def part1(d, preamble=25): return invalid(list(map(int, d.split())), preamble)[0]


def part2(d, preamble=25):
    nums = list(map(int, d.split()));
    target, end = invalid(nums, preamble)
    for start in range(end):
        total = 0
        for stop in range(start, end):
            total += nums[stop]
            if total == target and stop > start: return min(nums[start:stop + 1]) + max(nums[start:stop + 1])
            if total > target: break
    raise ValueError("No contiguous range sums to the invalid value")


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
