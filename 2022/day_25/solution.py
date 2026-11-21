from pathlib import Path


def decode(s):
    n = 0
    for c in s: n = n * 5 + {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}[c]
    return n


def encode(n):
    if n == 0: return "0"
    out = ""
    while n:
        n, r = divmod(n + 2, 5);
        out = "=-012"[r] + out
    return out


def part1(d): return encode(sum(decode(x.strip()) for x in d.splitlines() if x.strip()))


def part2(d): return "Merry Christmas!"


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
