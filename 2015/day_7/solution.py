from pathlib import Path


def run_circuit(lines: list[str], override_b: int | None = None) -> int:
    wires = {}
    for line in lines:
        if ' -> ' in line:
            expression, wire = line.split(' -> ')
            wires[wire] = expression
    if override_b is not None:
        wires['b'] = str(override_b)
    cache: dict[str, int] = {}

    def signal(token: str) -> int:
        if token.isdigit():
            return int(token)
        if token in cache:
            return cache[token]
        expr = wires[token].split()
        if len(expr) == 1:
            value = signal(expr[0])
        elif expr[0] == 'NOT':
            value = ~signal(expr[1])
        else:
            left, op, right = expr
            a, b = signal(left), signal(right)
            value = {'AND': a & b, 'OR': a | b, 'LSHIFT': a << b, 'RSHIFT': a >> b}[op]
        cache[token] = value & 0xffff
        return cache[token]

    return signal('a')


def solve(lines: list[str]) -> tuple[int, int]:
    first = run_circuit(lines)
    return first, run_circuit(lines, first)


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
