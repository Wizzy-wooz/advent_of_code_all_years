from pathlib import Path
import re


def run(d, floating=False):
    mem = {};
    mask = ""
    for line in d.splitlines():
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        elif line.strip():
            addr, val = map(int, re.findall(r"\d+", line))
            if not floating:
                bits = f"{val:036b}";
                mem[addr] = int("".join(b if m == "X" else m for b, m in zip(bits, mask)), 2)
            else:
                base = list(f"{addr:036b}");
                floats = []
                for i, m in enumerate(mask):
                    if m == "1":
                        base[i] = "1"
                    elif m == "X":
                        base[i] = "X";floats.append(i)
                for n in range(1 << len(floats)):
                    for j, p in enumerate(floats): base[p] = str(n >> (len(floats) - 1 - j) & 1)
                    mem[int("".join(base), 2)] = val
    return sum(mem.values())


def part1(d): return run(d)


def part2(d): return run(d, True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
