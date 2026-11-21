from pathlib import Path


def run(program: list[int], noun: int, verb: int) -> int:
    memory = program.copy();
    memory[1:3] = [noun, verb];
    ip = 0
    while memory[ip] != 99:
        op, a, b, c = memory[ip:ip + 4];
        memory[c] = memory[a] + memory[b] if op == 1 else memory[a] * memory[b];
        ip += 4
    return memory[0]


def part1(data: str) -> int: return run(list(map(int, data.strip().split(","))), 12, 2)


def part2(data: str) -> int:
    p = list(map(int, data.strip().split(",")))
    for n in range(100):
        for v in range(100):
            try:
                if run(p, n, v) == 19690720: return 100 * n + v
            except IndexError:
                pass
    raise ValueError("No noun/verb pair found")


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
