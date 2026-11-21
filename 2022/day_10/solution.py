from pathlib import Path


def run(d):
    x = 1;
    cycle = 0;
    signal = 0;
    screen = []

    def tick():
        nonlocal cycle, signal
        col = cycle % 40;
        screen.append("#" if abs(col - x) <= 1 else " ");
        cycle += 1
        if (cycle - 20) % 40 == 0: signal += cycle * x

    for line in d.splitlines():
        if not line.strip(): continue
        tick()
        if line.startswith("addx"): tick();x += int(line.split()[1])
    return signal, "\n".join("".join(screen[i:i + 40]).rstrip() for i in range(0, len(screen), 40))


def part1(d): return run(d)[0]


def part2(d): return run(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:\n" + part2(d))
