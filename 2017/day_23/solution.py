from collections import defaultdict
from pathlib import Path
import re


def run(data: str) -> int:
    code = [line.split() for line in data.splitlines() if line.strip()]
    registers = defaultdict(int)
    ip = mul_count = 0

    def val(token: str) -> int:
        try:
            return int(token)
        except ValueError:
            return registers[token]

    while 0 <= ip < len(code):
        op, x, *rest = code[ip]
        y = rest[0] if rest else None
        if op == "set":
            registers[x] = val(y)
        elif op == "sub":
            registers[x] -= val(y)
        elif op == "mul":
            registers[x] *= val(y); mul_count += 1
        elif op == "jnz" and val(x) != 0:
            ip += val(y)
            continue
        ip += 1
    return mul_count


def part1(data: str) -> int:
    return run(data)


def part2(data: str) -> int:
    code = [line.split() for line in data.splitlines() if line.strip()]
    # The puzzle program sets b to a constant, scales it, then counts composites
    # from b through c in fixed increments.
    start = next(int(tokens[2]) for tokens in code if tokens[:2] == ["set", "b"] and len(tokens) == 3)
    multiply = next(int(tokens[2]) for tokens in code if tokens[:2] == ["mul", "b"] and len(tokens) == 3)
    scale_adjust = next((int(t[2]) for t in code if t[:2] == ["sub", "b"] and len(t) == 3 and int(t[2]) < 0), None)
    end_adjust = next((int(t[2]) for t in code if t[:2] == ["sub", "c"] and len(t) == 3 and int(t[2]) < 0), None)
    step_adjust = next((int(t[2]) for t in code if
                        t[:2] == ["sub", "b"] and len(t) == 3 and int(t[2]) < 0 and int(t[2]) != scale_adjust), None)
    if scale_adjust is None or end_adjust is None or step_adjust is None:
        raise ValueError("Could not identify the composite-counting loop")
    first = start * multiply - scale_adjust
    last = first - end_adjust
    step = -step_adjust
    composites = 0
    for number in range(first, last + 1, step):
        if any(number % divisor == 0 for divisor in range(2, int(number ** 0.5) + 1)):
            composites += 1
    return composites


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
