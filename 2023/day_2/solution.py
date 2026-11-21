from pathlib import Path
import re


def games(d):
    for line in d.splitlines():
        if line.strip():
            i = int(re.search(r"Game (\d+)", line)[1]);
            sets = [{c: int(n) for n, c in re.findall(r"(\d+) (red|green|blue)", s)} for s in
                    line.split(":")[1].split(";")];
            yield i, sets


def part1(d): return sum(i for i, ss in games(d) if
                         all(s.get("red", 0) <= 12 and s.get("green", 0) <= 13 and s.get("blue", 0) <= 14 for s in ss))


def part2(d): return sum(
    max(s.get("red", 0) for s in ss) * max(s.get("green", 0) for s in ss) * max(s.get("blue", 0) for s in ss) for _, ss
    in games(d))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
