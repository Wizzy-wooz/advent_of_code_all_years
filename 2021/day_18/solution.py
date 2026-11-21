from itertools import permutations
from pathlib import Path
import ast


def flat(text):
    out = [];
    depth = 0
    for c in text:
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        elif c.isdigit():
            out.append([int(c), depth])
    return out


def reduce_num(a):
    while True:
        for i in range(len(a) - 1):
            if a[i][1] > 4 and a[i][1] == a[i + 1][1]:
                if i: a[i - 1][0] += a[i][0]
                if i + 2 < len(a): a[i + 2][0] += a[i + 1][0]
                a[i:i + 2] = [[0, a[i][1] - 1]];
                break
        else:
            for i, (n, dep) in enumerate(a):
                if n >= 10: a[i:i + 1] = [[n // 2, dep + 1], [(n + 1) // 2, dep + 1]];break
            else:
                return a
            continue
        continue


def magnitude(a):
    a = [x[:] for x in a]
    while len(a) > 1:
        dep = max(x[1] for x in a);
        i = next(i for i in range(len(a) - 1) if a[i][1] == dep and a[i + 1][1] == dep)
        a[i:i + 2] = [[3 * a[i][0] + 2 * a[i + 1][0], dep - 1]]
    return a[0][0]


def solve(d):
    nums = [flat(x) for x in d.splitlines() if x.strip()];
    total = nums[0]
    for n in nums[1:]: total = reduce_num([[v, dep + 1] for v, dep in total + n])
    return magnitude(total), max(
        magnitude(reduce_num([[v, dep + 1] for v, dep in a + b])) for a, b in permutations(nums, 2))


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
