from pathlib import Path


def enhance(d, steps):
    algorithm, raw = d.strip().split("\n\n")
    pixels = [[c == "#" for c in row] for row in raw.splitlines()]
    background = False
    for _ in range(steps):
        width = len(pixels[0]) + 4
        border = [background] * width
        padded = [border, border]
        padded.extend([background, background, *row, background, background] for row in pixels)
        padded.extend([border, border])
        pixels = []
        for y in range(1, len(padded) - 1):
            row = []
            for x in range(1, width - 1):
                index = 0
                for yy in range(y - 1, y + 2):
                    for xx in range(x - 1, x + 2):
                        index = (index << 1) | padded[yy][xx]
                row.append(algorithm[index] == "#")
            pixels.append(row)
        background = algorithm[511 if background else 0] == "#"
    if background:
        raise ValueError("Infinite number of lit pixels after requested enhancement")
    return sum(map(sum, pixels))


def part1(d): return enhance(d, 2)


def part2(d): return enhance(d, 50)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
