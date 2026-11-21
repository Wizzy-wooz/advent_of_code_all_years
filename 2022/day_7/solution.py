from collections import defaultdict
from pathlib import Path


def sizes(d):
    path = [];
    tot = defaultdict(int)
    for line in d.splitlines():
        if line.startswith("$ cd "):
            dest = line[5:]
            if dest == "/":
                path = []
            elif dest == "..":
                path.pop()
            else:
                path.append(dest)
        elif line and line[0].isdigit():
            n = int(line.split()[0])
            for i in range(len(path) + 1): tot[tuple(path[:i])] += n
    return list(tot.values())


def part1(d): return sum(x for x in sizes(d) if x <= 100000)


def part2(d):
    s = sizes(d);
    need = 30000000 - (70000000 - max(s));
    return min(x for x in s if x >= need)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
