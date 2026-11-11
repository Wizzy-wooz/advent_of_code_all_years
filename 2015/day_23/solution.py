from pathlib import Path


def run(program: list[str], initial_a: int = 0) -> dict[str, int]:
    registers = {'a': initial_a, 'b': 0}
    ip = 0
    while 0 <= ip < len(program):
        parts = program[ip].replace(',', '').split()
        op, register = parts[0], parts[1]
        if op == 'hlf':
            registers[register] //= 2
            ip += 1
        elif op == 'tpl':
            registers[register] *= 3
            ip += 1
        elif op == 'inc':
            registers[register] += 1
            ip += 1
        elif op == 'jmp':
            ip += int(register)
        elif op == 'jie':
            ip += int(parts[2]) if registers[register] % 2 == 0 else 1
        elif op == 'jio':
            ip += int(parts[2]) if registers[register] == 1 else 1
        else:
            raise ValueError(f'Unknown instruction: {program[ip]}')
    return registers


def solve(lines: list[str]) -> tuple[int, int]:
    return run(lines)['b'], run(lines, initial_a=1)['b']


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
