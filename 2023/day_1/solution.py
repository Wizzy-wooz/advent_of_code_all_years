from pathlib import Path

WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def values(s, words=False):
    out = []
    for i, c in enumerate(s):
        if c.isdigit():
            out.append(int(c))
        elif words:
            for w, n in WORDS.items():
                if s.startswith(w, i): out.append(n);break
    return 10 * out[0] + out[-1]


def part1(d): return sum(values(x) for x in d.splitlines() if x)


def part2(d): return sum(values(x, True) for x in d.splitlines() if x)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
