from pathlib import Path
import re


def parse(d):
    a, b = d.split("\n\n");
    rules = {}
    for line in a.splitlines():
        n, s = line.split(": ");
        rules[n] = s
    return rules, b.splitlines()


def matches(message, rules):
    memo = {}

    def ends(rule, pos):
        key = (rule, pos)
        if key in memo: return memo[key]
        text = rules[rule]
        if '"' in text:
            result = {pos + 1} if pos < len(message) and message[pos] == text[1] else set()
        else:
            result = set()
            for option in text.split(" | "):
                positions = {pos}
                for r in option.split(): positions = {j for i in positions for j in ends(r, i)}
                result |= positions
        memo[key] = result;
        return result

    return len(message) in ends("0", 0)


def solve(d, recursive=False):
    rules, messages = parse(d)
    if recursive:
        rules["8"] = "42 | 42 8";
        rules["11"] = "42 31 | 42 11 31"
    return sum(matches(m, rules) for m in messages)


def part1(d): return solve(d)


def part2(d): return solve(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
