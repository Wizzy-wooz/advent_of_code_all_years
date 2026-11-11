from pathlib import Path


def parse_boxes(text: str) -> list[tuple[int, int, int]]:
    boxes = []
    for line in text.splitlines():
        if line.strip():
            length, width, height = map(int, line.split('x'))
            boxes.append((length, width, height))
    return boxes


def part1(boxes: list[tuple[int, int, int]]) -> int:
    total = 0
    for length, width, height in boxes:
        sides = (length * width, width * height, height * length)
        total += 2 * sum(sides) + min(sides)
    return total


def part2(boxes: list[tuple[int, int, int]]) -> int:
    total = 0
    for dimensions in boxes:
        shortest_sides = sorted(dimensions)[:2]
        length, width, height = dimensions
        total += 2 * sum(shortest_sides) + length * width * height
    return total


if __name__ == '__main__':
    input_path = Path(__file__).with_name('input.txt')
    boxes = parse_boxes(input_path.read_text())
    print(f'Part 1: {part1(boxes)}')
    print(f'Part 2: {part2(boxes)}')
