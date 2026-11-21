from pathlib import Path

BASE = (0, 1, 0, -1)


def part1(data):
    digits = list(map(int, data.strip()))
    for _ in range(100):
        digits = [abs(sum(v * BASE[((j + 1) // (i + 1)) % 4] for j, v in enumerate(digits))) % 10 for i in
                  range(len(digits))]
    return "".join(map(str, digits[:8]))


def part2(data):
    base = list(map(int, data.strip()));
    offset = int(data.strip()[:7]);
    n = len(base) * 10000
    if offset < n // 2: raise ValueError("Optimized suffix method requires offset in the latter half")
    signal = (base * (10000))[offset:]
    for _ in range(100):
        total = 0
        for i in range(len(signal) - 1, -1, -1): total = (total + signal[i]) % 10;signal[i] = total
    return "".join(map(str, signal[:8]))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
