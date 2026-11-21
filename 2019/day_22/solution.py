from pathlib import Path
import re


def shuffle(data, size):
    deck = list(range(size))
    for line in data.splitlines():
        if line.startswith("deal into new stack"):
            deck.reverse()
        elif line.startswith("cut "):
            n = int(line.split()[-1]);
            deck = deck[n:] + deck[:n]
        elif line.startswith("deal with increment "):
            n = int(line.split()[-1]);
            new = [0] * size
            for i, c in enumerate(deck): new[(i * n) % size] = c
            deck = new
    return deck


def part1(data): return shuffle(data, 10007).index(2019)


def part2(data):
    m = 119315717514047;
    reps = 101741582076661;
    a, b = 1, 0
    for line in data.splitlines():
        if line.startswith("deal into new stack"):
            a, b = -a % m, (-b - 1) % m
        elif line.startswith("cut "):
            b = (b - int(line.split()[-1])) % m
        elif line.startswith("deal with increment "):
            n = int(line.split()[-1]);
            a, b = a * n % m, b * n % m
    ar = pow(a, reps, m);
    br = b * (ar - 1) * pow(a - 1, -1, m) % m if a != 1 else b * reps % m
    return (2020 - br) * pow(ar, -1, m) % m


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
