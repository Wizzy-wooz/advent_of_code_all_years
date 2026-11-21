from pathlib import Path


def parse(d):
    a, b = d.strip().split("\n\n");
    vals = {x: int(v) for x, v in (l.split(": ") for l in a.splitlines())};
    g = {}
    for l in b.splitlines(): x, op, y, _, z = l.split();g[z] = (x, op, y)
    return vals, g


def part1(d):
    vals, g = parse(d)
    while True:
        changed = False
        for z, (x, op, y) in g.items():
            if z not in vals and x in vals and y in vals: vals[z] = \
            {"AND": vals[x] & vals[y], "OR": vals[x] | vals[y], "XOR": vals[x] ^ vals[y]}[op];changed = True
        if not changed: break
    return sum(v << int(k[1:]) for k, v in vals.items() if k.startswith("z"))


def part2(d):
    _, g = parse(d);
    bad = set()
    for out, (a, op, b) in g.items():
        if out.startswith("z") and out != "z45" and op != "XOR": bad.add(out)
        if op == "XOR" and not out.startswith("z") and not (a[0] in "xy" and b[0] in "xy"): bad.add(out)
        if op == "AND" and "x00" not in (a, b) and any(
            out in pair for pair in g.values() if pair[1] == "OR") == False: bad.add(out)
    return ",".join(sorted(bad))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
