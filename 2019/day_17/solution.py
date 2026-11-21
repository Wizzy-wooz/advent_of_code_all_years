from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]));
from intcode import Computer


def camera(data):
    out = Computer(list(map(int, data.strip().split(",")))).run();
    return [list(line) for line in "".join(map(chr, out)).strip().splitlines()]


def part1(data):
    g = camera(data);
    return sum(x * y for y in range(1, len(g) - 1) for x in range(1, len(g[y]) - 1) if
               g[y][x] == "#" and all(g[ny][nx] == "#" for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))))


def path_tokens(g):
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)];
    sc = {"^": 0, ">": 1, "v": 2, "<": 3}
    y, x, d = next((y, x, sc[c]) for y, row in enumerate(g) for x, c in enumerate(row) if c in sc);
    tokens = []
    while True:
        if g[y + dirs[(d + 1) % 4][1]][x + dirs[(d + 1) % 4][0]] == "#":
            d = (d + 1) % 4;tokens.append("R")
        elif g[y + dirs[(d - 1) % 4][1]][x + dirs[(d - 1) % 4][0]] == "#":
            d = (d - 1) % 4;tokens.append("L")
        else:
            break
        dx, dy = dirs[d];
        n = 0
        while 0 <= y + dy < len(g) and 0 <= x + dx < len(g[y + dy]) and g[y + dy][x + dx] == "#": x += dx;y += dy;n += 1
        tokens.append(str(n))
    return tokens


def compress(tokens):
    def search(i, funcs, main):
        if i == len(tokens): return main, funcs
        for name, seq in funcs.items():
            if tokens[i:i + len(seq)] == seq and len(",".join(main + [name])) <= 20:
                ans = search(i + len(seq), funcs, main + [name])
                if ans: return ans
        if len(funcs) == 3: return None
        name = chr(65 + len(funcs))
        for end in range(i + 2, len(tokens) + 1, 2):
            seq = tokens[i:end]
            if len(",".join(seq)) > 20: break
            ans = search(end, {**funcs, name: seq}, main + [name])
            if ans: return ans
        return None

    result = search(0, {}, [])
    if not result: raise ValueError("Could not compress scaffold route")
    return result


def part2(data):
    p = list(map(int, data.strip().split(",")));
    g = camera(data);
    main, funcs = compress(path_tokens(g));
    lines = [",".join(main)] + [",".join(funcs.get(k, [])) for k in "ABC"] + ["n"]
    p[0] = 2;
    c = Computer(p, [ord(ch) for ch in "\n".join(lines) + "\n"]);
    return c.run()[-1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
