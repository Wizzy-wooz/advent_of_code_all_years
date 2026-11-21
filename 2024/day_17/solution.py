from pathlib import Path
import re


def parse(d): a, b = d.split("\n\n");return list(map(int, re.findall(r"\d+", a))), list(map(int, re.findall(r"\d+", b)))


def execute(reg, prog):
    a, b, c = reg;
    ip = 0;
    out = []
    while ip < len(prog):
        op, arg = prog[ip:ip + 2];
        combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c}.get(arg, arg)
        if op == 0:
            a //= 2 ** combo
        elif op == 1:
            b ^= arg
        elif op == 2:
            b = combo % 8
        elif op == 3:
            if a: ip = arg;continue
        elif op == 4:
            b ^= c
        elif op == 5:
            out.append(combo % 8)
        elif op == 6:
            b = a // (2 ** combo)
        elif op == 7:
            c = a // (2 ** combo)
        ip += 2
    return out


def part1(d): r, p = parse(d);return ",".join(map(str, execute(r, p)))


def part2(d):
    _, p = parse(d);
    candidates = {0}
    for i in range(len(p) - 1, -1, -1):
        candidates = {a * 8 + x for a in candidates for x in range(8) if execute((a * 8 + x, 0, 0), p) == p[i:]}
    return min(candidates)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
