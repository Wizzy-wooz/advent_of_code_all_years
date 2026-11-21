from pathlib import Path


def value_after(data: str, minutes: int) -> int:
    grid = tuple(line.strip() for line in data.splitlines() if line.strip());
    seen = {};
    t = 0
    while t < minutes:
        if grid in seen:
            cycle = t - seen[grid];
            skip = (minutes - t) // cycle
            if skip: t += skip * cycle; continue
        else:
            seen[grid] = t
        h, w = len(grid), len(grid[0]);
        new = []
        for y in range(h):
            row = ""
            for x in range(w):
                adjacent = [grid[ny][nx] for ny in range(max(0, y - 1), min(h, y + 2)) for nx in
                            range(max(0, x - 1), min(w, x + 2)) if (nx, ny) != (x, y)]
                trees, yards = adjacent.count("|"), adjacent.count("#")
                if grid[y][x] == ".":
                    row += "|" if trees >= 3 else "."
                elif grid[y][x] == "|":
                    row += "#" if yards >= 3 else "|"
                else:
                    row += "#" if yards >= 1 and trees >= 1 else "."
            new.append(row)
        grid = tuple(new);
        t += 1
    return sum(row.count("|") for row in grid) * sum(row.count("#") for row in grid)


def part1(data: str) -> int: return value_after(data, 10)


def part2(data: str) -> int: return value_after(data, 1_000_000_000)


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
