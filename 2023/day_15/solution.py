from pathlib import Path


def hashv(s):
    v = 0
    for c in s: v = (v + ord(c)) * 17 % 256
    return v


def part1(d): return sum(hashv(x) for x in d.strip().split(","))


def part2(d):
    boxes = [[] for _ in range(256)]
    for ins in d.strip().split(","):
        if ins.endswith("-"):
            label = ins[:-1];
            b = boxes[hashv(label)];
            b[:] = [(k, v) for k, v in b if k != label]
        else:
            label, n = ins.split("=");
            b = boxes[hashv(label)]
            for i, (k, v) in enumerate(b):
                if k == label: b[i] = (label, int(n));break
            else:
                b.append((label, int(n)))
    return sum((i + 1) * (j + 1) * v for i, b in enumerate(boxes) for j, (_, v) in enumerate(b))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
