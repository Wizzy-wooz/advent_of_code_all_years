from pathlib import Path


def possible(target, nums, concat):
    states = {nums[0]}
    for n in nums[1:]:
        states = {v for x in states for v in (x + n, x * n, int(str(x) + str(n)) if concat else -1) if v <= target}
    return target in states


def solve(d):
    a = b = 0
    for line in d.splitlines():
        if line.strip(): t, s = line.split(":");target = int(t);nums = list(map(int, s.split()));a += target * possible(
            target, nums, False);b += target * possible(target, nums, True)
    return a, b


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
