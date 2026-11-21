from pathlib import Path


def execute(data: str, initial_a: int = 0, limit: int = 10_000_000) -> list[int]:
    lines = data.splitlines();
    ip_register = int(lines[0].split()[1]);
    program = [line.split() for line in lines[1:] if line.strip()]
    regs = [0] * 6;
    regs[0] = initial_a;
    ip = 0

    def op(name, a, b, c):
        if name == "addr":
            regs[c] = regs[a] + regs[b]
        elif name == "addi":
            regs[c] = regs[a] + b
        elif name == "mulr":
            regs[c] = regs[a] * regs[b]
        elif name == "muli":
            regs[c] = regs[a] * b
        elif name == "banr":
            regs[c] = regs[a] & regs[b]
        elif name == "bani":
            regs[c] = regs[a] & b
        elif name == "borr":
            regs[c] = regs[a] | regs[b]
        elif name == "bori":
            regs[c] = regs[a] | b
        elif name == "setr":
            regs[c] = regs[a]
        elif name == "seti":
            regs[c] = a
        elif name == "gtir":
            regs[c] = int(a > regs[b])
        elif name == "gtri":
            regs[c] = int(regs[a] > b)
        elif name == "gtrr":
            regs[c] = int(regs[a] > regs[b])
        elif name == "eqir":
            regs[c] = int(a == regs[b])
        elif name == "eqri":
            regs[c] = int(regs[a] == b)
        elif name == "eqrr":
            regs[c] = int(regs[a] == regs[b])

    for _ in range(limit):
        if not 0 <= ip < len(program): return regs
        regs[ip_register] = ip
        name, a, b, c = program[ip];
        op(name, int(a), int(b), int(c));
        ip = regs[ip_register] + 1
    return regs


def part1(data: str) -> int: return execute(data)[0]


def part2(data: str) -> int:
    # In the puzzle program, the nested loops sum divisors of the large target in r3.
    regs = execute(data, 1, 1000);
    target = max(regs)
    if target <= 0: return regs[0]
    return sum(d + (target // d if d * d != target else 0) for d in range(1, int(target ** 0.5) + 1) if target % d == 0)


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
