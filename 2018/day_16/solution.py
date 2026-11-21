from collections import defaultdict
from pathlib import Path
import re

OPS = ("addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir",
       "eqri", "eqrr")


def apply(op, before, a, b, c):
    r = before.copy()
    if op == "addr":
        r[c] = r[a] + r[b]
    elif op == "addi":
        r[c] = r[a] + b
    elif op == "mulr":
        r[c] = r[a] * r[b]
    elif op == "muli":
        r[c] = r[a] * b
    elif op == "banr":
        r[c] = r[a] & r[b]
    elif op == "bani":
        r[c] = r[a] & b
    elif op == "borr":
        r[c] = r[a] | r[b]
    elif op == "bori":
        r[c] = r[a] | b
    elif op == "setr":
        r[c] = r[a]
    elif op == "seti":
        r[c] = a
    elif op == "gtir":
        r[c] = int(a > r[b])
    elif op == "gtri":
        r[c] = int(r[a] > b)
    elif op == "gtrr":
        r[c] = int(r[a] > r[b])
    elif op == "eqir":
        r[c] = int(a == r[b])
    elif op == "eqri":
        r[c] = int(r[a] == b)
    elif op == "eqrr":
        r[c] = int(r[a] == r[b])
    return r


def parse(data: str):
    samples_text, _, program_text = data.partition("\n\n\n")
    samples = []
    for block in re.findall(r"Before:.*?After:.*?(?=\n\s*\n|$)", samples_text, re.S):
        nums = list(map(int, re.findall(r"\d+", block)))
        samples.append((nums[:4], nums[4:8], nums[8:12]))
    program = [list(map(int, line.split())) for line in program_text.splitlines() if line.strip()]
    return samples, program


def solve(data: str):
    samples, program = parse(data);
    possible = defaultdict(lambda: set(OPS));
    three = 0
    for before, instruction, after in samples:
        code, a, b, c = instruction
        matching = {op for op in OPS if apply(op, before, a, b, c) == after}
        three += len(matching) >= 3;
        possible[code] &= matching
    mapping = {}
    while len(mapping) < len(possible):
        singles = [(code, next(iter(opts))) for code, opts in possible.items() if
                   code not in mapping and len(opts) == 1]
        for code, op in singles:
            mapping[code] = op
            for other in possible:
                if other != code: possible[other].discard(op)
    registers = [0] * 4
    for code, a, b, c in program: registers = apply(mapping[code], registers, a, b, c)
    return three, registers[0]


def part1(data: str) -> int: return solve(data)[0]


def part2(data: str) -> int: return solve(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
