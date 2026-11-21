from pathlib import Path


def parse(d): return [(a, int(b)) for a, b in (x.split() for x in d.splitlines() if x.strip())]


def execute(p, swap=-1):
    acc = ip = 0;
    seen = set()
    while ip not in seen and 0 <= ip < len(p):
        seen.add(ip);
        op, n = p[ip]
        if ip == swap: op = "nop" if op == "jmp" else "jmp" if op == "nop" else op
        if op == "acc":
            acc += n;ip += 1
        elif op == "jmp":
            ip += n
        else:
            ip += 1
    return acc, ip == len(p)


def part1(d): return execute(parse(d))[0]


def part2(d):
    p = parse(d)
    for i, (op, _) in enumerate(p):
        if op in ("jmp", "nop"):
            acc, ok = execute(p, i)
            if ok: return acc
    raise ValueError("No single instruction swap fixes the program")


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
