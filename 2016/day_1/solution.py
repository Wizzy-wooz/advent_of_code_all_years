from pathlib import Path


def part1(instructions: str) -> int:
    # Directions are north, east, south, west.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    facing = 0
    x = y = 0

    for instruction in instructions.split(','):
        instruction = instruction.strip()
        turn, blocks = instruction[0], int(instruction[1:])
        facing = (facing + (1 if turn == 'R' else -1)) % 4
        dx, dy = directions[facing]
        x += dx * blocks
        y += dy * blocks

    return abs(x) + abs(y)


def part2(instructions: str) -> int | None:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    facing = 0
    x = y = 0
    visited = {(x, y)}

    # Move one block at a time so we can detect the first repeated location.
    for instruction in instructions.split(','):
        instruction = instruction.strip()
        turn, blocks = instruction[0], int(instruction[1:])
        facing = (facing + (1 if turn == 'R' else -1)) % 4
        dx, dy = directions[facing]

        for _ in range(blocks):
            x += dx
            y += dy
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))

    return None


if __name__ == '__main__':
    instructions = Path(__file__).with_name('input.txt').read_text().strip()
    print(f'Part 1: {part1(instructions)}')
    answer = part2(instructions)
    print(f'Part 2: {answer if answer is not None else "no location visited twice"}')
