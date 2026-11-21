from pathlib import Path


def part1(d):
    blocks = [b.splitlines() for b in d.strip().split("\n\n")];
    locks = [];
    keys = []
    for b in blocks:
        heights = tuple(sum(row[x] == "#" for row in b) - 1 for x in range(len(b[0])))
        (locks if b[0][0] == "#" else keys).append(heights)
    return sum(all(a + b <= len(blocks[0]) - 2 for a, b in zip(lock, key)) for lock in locks for key in keys)


def part2(d): return "Merry Christmas!"


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
