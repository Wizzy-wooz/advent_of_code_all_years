from pathlib import Path


MOVES = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
}


def visit_houses(directions: str, santa_count: int = 1) -> int:
    positions = [(0, 0)] * santa_count
    visited = {(0, 0)}

    for step, direction in enumerate(directions):
        if direction not in MOVES:
            continue

        santa = step % santa_count
        x, y = positions[santa]
        dx, dy = MOVES[direction]
        positions[santa] = (x + dx, y + dy)
        visited.add(positions[santa])

    return len(visited)


def part1(directions: str) -> int:
    return visit_houses(directions)


def part2(directions: str) -> int:
    return visit_houses(directions, santa_count=2)


if __name__ == '__main__':
    directions = Path(__file__).with_name('input.txt').read_text().strip()
    print(f'Part 1: {part1(directions)}')
    print(f'Part 2: {part2(directions)}')
