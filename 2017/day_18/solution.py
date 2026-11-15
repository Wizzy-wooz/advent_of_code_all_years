from collections import defaultdict, deque
from pathlib import Path

def value(token: str, registers: dict[str, int]) -> int:
    try:
        return int(token)
    except ValueError:
        return registers[token]

def recover_frequency(data: str) -> int:
    code = [line.split() for line in data.splitlines() if line.strip()]
    registers: dict[str, int] = defaultdict(int)
    sound = ip = 0
    while 0 <= ip < len(code):
        op, x, *rest = code[ip]
        y = rest[0] if rest else None
        if op == "snd": sound = registers[x]
        elif op == "set": registers[x] = value(y, registers)
        elif op == "add": registers[x] += value(y, registers)
        elif op == "mul": registers[x] *= value(y, registers)
        elif op == "mod": registers[x] %= value(y, registers)
        elif op == "rcv" and registers[x] != 0: return sound
        elif op == "jgz" and value(x, registers) > 0:
            ip += value(y, registers)
            continue
        ip += 1
    raise ValueError("Program terminated without recovering a sound")

def duet_sends(data: str) -> int:
    code = [line.split() for line in data.splitlines() if line.strip()]
    regs = [defaultdict(int, {"p": i}) for i in range(2)]
    queues = [deque(), deque()]
    ips, sends, waiting = [0, 0], [0, 0], [False, False]
    def val(token: str, pid: int) -> int: return value(token, regs[pid])
    while True:
        progressed = False
        for pid in range(2):
            if not 0 <= ips[pid] < len(code):
                waiting[pid] = True
                continue
            op, x, *rest = code[ips[pid]]
            y = rest[0] if rest else None
            if op == "rcv" and not queues[pid]:
                waiting[pid] = True
                continue
            waiting[pid] = False
            progressed = True
            if op == "snd": queues[1 - pid].append(val(x, pid)); sends[pid] += 1
            elif op == "set": regs[pid][x] = val(y, pid)
            elif op == "add": regs[pid][x] += val(y, pid)
            elif op == "mul": regs[pid][x] *= val(y, pid)
            elif op == "mod": regs[pid][x] %= val(y, pid)
            elif op == "rcv": regs[pid][x] = queues[pid].popleft()
            elif op == "jgz" and val(x, pid) > 0:
                ips[pid] += val(y, pid)
                continue
            ips[pid] += 1
        if not progressed and all(waiting): return sends[1]

def part1(data: str) -> int: return recover_frequency(data)
def part2(data: str) -> int: return duet_sends(data)

if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
