from pathlib import Path


def solve(d):
    easy = total = 0
    for line in d.splitlines():
        if not line.strip(): continue
        left, right = line.split(" | ");
        patterns = [set(x) for x in left.split()];
        nums = {len(x): x for x in patterns if len(x) in (2, 3, 4, 7)};
        one, two = nums[2], nums[4]
        m = {1: nums[2], 4: nums[4], 7: nums[3], 8: nums[7]};
        m[9] = next(x for x in patterns if len(x) == 6 and two <= x);
        m[0] = next(x for x in patterns if len(x) == 6 and one <= x and x != m[9]);
        m[6] = next(x for x in patterns if len(x) == 6 and x not in (m[0], m[9]));
        m[3] = next(x for x in patterns if len(x) == 5 and one <= x);
        m[5] = next(x for x in patterns if len(x) == 5 and x <= m[6]);
        m[2] = next(x for x in patterns if len(x) == 5 and x not in (m[3], m[5]));
        rev = {frozenset(v): str(k) for k, v in m.items()};
        easy += sum(len(x) in (2, 3, 4, 7) for x in right.split());
        total += int("".join(rev[frozenset(x)] for x in right.split()))
    return easy, total


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
