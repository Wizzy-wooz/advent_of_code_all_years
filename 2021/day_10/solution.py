from pathlib import Path

PAIRS = {")": "(", "]": "[", "}": "{", ">": "<"};
SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137};
COMP = {"(": 1, "[": 2, "{": 3, "<": 4}


def solve(d):
    a = [];
    b = []
    for line in d.splitlines():
        st = []
        for c in line:
            if c in PAIRS.values():
                st.append(c)
            elif not st or st.pop() != PAIRS[c]:
                a.append(SCORE[c]);break
        else:
            if st:
                n = 0
                for c in reversed(st): n = n * 5 + COMP[c]
                b.append(n)
    return sum(a), sorted(b)[len(b) // 2]


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
