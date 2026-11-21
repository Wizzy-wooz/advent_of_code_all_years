from pathlib import Path


def packet(bits, pos=0):
    ver = int(bits[pos:pos + 3], 2);
    typ = int(bits[pos + 3:pos + 6], 2);
    pos += 6;
    versions = ver
    if typ == 4:
        value = 0
        while True:
            group = bits[pos:pos + 5];
            pos += 5;
            value = value * 16 + int(group[1:], 2)
            if group[0] == "0": break
        return versions, value, pos
    vals = []
    if bits[pos] == "0":
        end = pos + 16 + int(bits[pos + 1:pos + 16], 2);
        pos += 16
        while pos < end: v, x, pos = packet(bits, pos);versions += v;vals.append(x)
    else:
        count = int(bits[pos + 1:pos + 12], 2);
        pos += 12
        for _ in range(count): v, x, pos = packet(bits, pos);versions += v;vals.append(x)
    value = \
    {0: sum, 1: __import__("math").prod, 2: min, 3: max, 5: lambda a: int(a[0] > a[1]), 6: lambda a: int(a[0] < a[1]),
     7: lambda a: int(a[0] == a[1])}[typ](vals)
    return versions, value, pos


def solve(d): return packet("".join(f"{int(c, 16):04b}" for c in d.strip()))[:2]


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
