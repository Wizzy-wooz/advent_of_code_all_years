from pathlib import Path


def simulate(d):
    g = [list(map(int, r.strip())) for r in d.splitlines() if r.strip()];
    h = len(g);
    w = len(g[0]);
    total = step = 0;
    sync = None
    while sync is None:
        step += 1;
        flash = set();
        stack = []
        for y in range(h):
            for x in range(w): g[y][x] += 1
            for x in range(w):
                if g[y][x] > 9: stack.append((x, y))
        while stack:
            x, y = stack.pop()
            if (x, y) in flash or g[y][x] <= 9: continue
            flash.add((x, y))
            for ny in range(max(0, y - 1), min(h, y + 2)):
                for nx in range(max(0, x - 1), min(w, x + 2)):
                    if (nx, ny) != (x, y): g[ny][nx] += 1
                    if g[ny][nx] > 9 and (nx, ny) not in flash: stack.append((nx, ny))
        for x, y in flash: g[y][x] = 0
        if step <= 100: total += len(flash)
        if len(flash) == h * w: sync = step
    return total, sync


def part1(d): return simulate(d)[0]


def part2(d): return simulate(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
