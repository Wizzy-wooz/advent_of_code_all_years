from pathlib import Path


def part1(d):
    g = [list(r) for r in d.splitlines() if r.strip()];
    h = len(g);
    w = len(g[0]);
    step = 0
    while True:
        step += 1;
        moved = False;
        east = [r.copy() for r in g]
        for y in range(h):
            for x in range(w):
                if g[y][x] == ">" and g[y][(x + 1) % w] == ".": east[y][x] = ".";east[y][(x + 1) % w] = ">";moved = True
        south = [r.copy() for r in east]
        for y in range(h):
            for x in range(w):
                if east[y][x] == "v" and east[(y + 1) % h][x] == ".": south[y][x] = ".";south[(y + 1) % h][
                    x] = "v";moved = True
        if not moved: return step
        g = south


def part2(d): return "Merry Christmas!"


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
