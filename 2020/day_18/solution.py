from pathlib import Path
import re


def evaluate(s, precedence):
    tokens = re.findall(r"\d+|[()+*]", s);
    values = [];
    ops = []
    prec = {"+": 2 if precedence else 1, "*": 1, "(": 0}
    for t in tokens:
        if t.isdigit():
            values.append(int(t))
        elif t == "(":
            ops.append(t)
        elif t == ")":
            while ops[-1] != "(": apply(values, ops.pop())
            ops.pop()
        else:
            while ops and prec[ops[-1]] >= prec[t]: apply(values, ops.pop())
            ops.append(t)
    while ops: apply(values, ops.pop())
    return values[0]


def apply(v, op):
    b = v.pop();
    a = v.pop();
    v.append(a + b if op == "+" else a * b)


def part1(d): return sum(evaluate(x, False) for x in d.splitlines() if x.strip())


def part2(d): return sum(evaluate(x, True) for x in d.splitlines() if x.strip())


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
