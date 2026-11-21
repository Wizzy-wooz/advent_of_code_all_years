from pathlib import Path


def safe(a):
    dif = [y - x for x, y in zip(a, a[1:])];
    return all(1 <= x <= 3 for x in dif) or all(-3 <= x <= -1 for x in dif)


def part1(d): return sum(safe(list(map(int, l.split()))) for l in d.splitlines() if l.strip())


def part2(d): return sum(any(safe(a[:i] + a[i + 1:]) for i in range(len(a))) or safe(a) for a in
                         (list(map(int, l.split())) for l in d.splitlines() if l.strip()))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
