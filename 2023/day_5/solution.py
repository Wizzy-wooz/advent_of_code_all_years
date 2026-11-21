from pathlib import Path


def parse(d):
    a, *blocks = d.strip().split("\n\n");
    return list(map(int, a.split(":")[1].split())), [[tuple(map(int, l.split())) for l in b.splitlines()[1:]] for b in
                                                     blocks]


def part1(d):
    seeds, maps = parse(d);
    vals = seeds[:]
    for mp in maps: vals = [next((dst + x - src for dst, src, n in mp if src <= x < src + n), x) for x in vals]
    return min(vals)


def part2(d):
    seeds, maps = parse(d);
    ranges = list(zip(seeds[::2], seeds[1::2]))
    for mp in maps:
        out = []
        for start, length in ranges:
            todo = [(start, start + length)]
            for dst, src, n in mp:
                rest = []
                for a, b in todo:
                    lo = max(a, src);
                    hi = min(b, src + n)
                    if lo < hi:
                        out.append((dst + lo - src, hi - lo));rest.extend(((a, lo), (hi, b)))
                    else:
                        rest.append((a, b))
                todo = rest
            out.extend((a, b - a) for a, b in todo if a < b)
        ranges = out
    return min(a for a, n in ranges)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
