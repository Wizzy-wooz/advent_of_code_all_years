from pathlib import Path


def expand(d):
    a = []
    for i, c in enumerate(d.strip()): a.extend([i // 2 if i % 2 == 0 else None] * int(c))
    return a


def part1(d):
    a = expand(d);
    l = 0;
    r = len(a) - 1
    while l < r:
        while l < len(a) and a[l] is not None: l += 1
        while r >= 0 and a[r] is None: r -= 1
        if l < r: a[l], a[r] = a[r], None
    return sum(i * x for i, x in enumerate(a) if x is not None)


def part2(d):
    a = expand(d);
    files = max((x for x in a if x is not None), default=-1)
    for f in range(files, -1, -1):
        inds = [i for i, x in enumerate(a) if x == f]
        if not inds: continue
        n = len(inds);
        start = next((i for i in range(inds[0]) if a[i:i + n] == [None] * n), None)
        if start is not None:
            for i in inds: a[i] = None
            a[start:start + n] = [f] * n
    return sum(i * x for i, x in enumerate(a) if x is not None)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text()
    ##print("Part 1:", part1(d))
    print("Part 2:", part2(d))
