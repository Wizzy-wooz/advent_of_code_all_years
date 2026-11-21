from pathlib import Path


def enhance(d, steps):
    algo, raw = d.strip().split("\n\n");
    lit = {(x, y) for y, r in enumerate(raw.splitlines()) for x, c in enumerate(r) if c == "#"};
    background = "."
    for _ in range(steps):
        if not lit: break
        xs = [x for x, y in lit];
        ys = [y for x, y in lit];
        new = set()
        for y in range(min(ys) - 1, max(ys) + 2):
            for x in range(min(xs) - 1, max(xs) + 2):
                bits = "".join(
                    "1" if (xx, yy) in lit else ("1" if background == "#" else "0") for yy in range(y - 1, y + 2) for xx
                    in range(x - 1, x + 2));
                v = algo[int(bits, 2)]
                if v == "#": new.add((x, y))
        background = algo[0 if background == "." else 511];
        lit = new
        if background == "#": raise ValueError("Infinite number of lit pixels after requested enhancement")
    return len(lit)


def part1(d): return enhance(d, 2)


def part2(d): return enhance(d, 50)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
