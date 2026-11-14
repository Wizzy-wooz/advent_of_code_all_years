import re


def execute(data: str, c: int = 0) -> int:
    program = [line.split() for line in data.splitlines() if line.strip()]
    regs = dict.fromkeys('abcd', 0); regs['c'] = c; ip = 0
    def val(x): return int(x) if re.fullmatch(r'-?\d+', x) else regs[x]
    while 0 <= ip < len(program):
        op, *args = program[ip]
        if op == 'cpy':
            if args[1] in regs: regs[args[1]] = val(args[0])
        elif op == 'inc' and args[0] in regs: regs[args[0]] += 1
        elif op == 'dec' and args[0] in regs: regs[args[0]] -= 1
        elif op == 'jnz' and val(args[0]) != 0: ip += val(args[1]); continue
        ip += 1
    return regs['a']


def part1(data: str) -> int: return execute(data)
def part2(data: str) -> int: return execute(data, 1)


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
