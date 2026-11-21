from pathlib import Path


def solve(d):
    chunks = d.strip().split("\n\n");
    draw = list(map(int, chunks[0].split(",")));
    boards = [[list(map(int, line.split())) for line in b.splitlines()] for b in chunks[1:]];
    won = set();
    scores = []
    for n in draw:
        for i, b in enumerate(boards):
            if i in won: continue
            for r in b:
                if n in r: r[r.index(n)] = -1
            if any(all(x < 0 for x in r) for r in b) or any(all(b[y][x] < 0 for y in range(5)) for x in range(5)):
                won.add(i);
                scores.append(n * sum(x for r in b for x in r if x >= 0))
    return scores[0], scores[-1]


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
