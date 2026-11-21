from pathlib import Path


def variants(pattern: tuple[str, ...]) -> set[tuple[str, ...]]:
    result = set()
    current = pattern
    for _ in range(4):
        result.add(current)
        result.add(tuple(row[::-1] for row in current))
        current = tuple("".join(row) for row in zip(*current[::-1]))
    return result


def parse(data: str) -> dict[tuple[str, ...], tuple[str, ...]]:
    rules = {}
    for line in data.splitlines():
        if line.strip():
            source, dest = line.split(" => ")
            output = tuple(dest.split("/"))
            for form in variants(tuple(source.split("/"))): rules[form] = output
    return rules


def enhance(data: str, iterations: int) -> int:
    rules = parse(data)
    grid = (".#.", "..#", "###")
    for _ in range(iterations):
        size = 2 if len(grid) % 2 == 0 else 3
        blocks = len(grid) // size
        output_size = size + 1
        result = [["" for _ in range(blocks * output_size)] for _ in range(blocks * output_size)]
        for br in range(blocks):
            for bc in range(blocks):
                square = tuple(grid[br * size + r][bc * size:bc * size + size] for r in range(size))
                replacement = rules[square]
                for r, row in enumerate(replacement): result[br * output_size + r][
                    bc * output_size:bc * output_size + output_size] = row
        grid = tuple("".join(row) for row in result)
    return sum(row.count("#") for row in grid)


def part1(data: str) -> int: return enhance(data, 5)


def part2(data: str) -> int: return enhance(data, 18)


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
