from pathlib import Path


def solve(instructions: str) -> tuple[int, int | None]:
    # Directions are north, east, south, west.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    facing = 0
    x = y = 0
    visited = {(x, y)}
    first_revisited_distance = None

    # Move one block at a time so we can detect the first repeated location.
    for instruction in instructions.split(','):
        instruction = instruction.strip()
        turn, blocks = instruction[0], int(instruction[1:])
        facing = (facing + (1 if turn == 'R' else -1)) % 4
        dx, dy = directions[facing]

        for _ in range(blocks):
            x += dx
            y += dy
            if first_revisited_distance is None and (x, y) in visited:
                first_revisited_distance = abs(x) + abs(y)
            visited.add((x, y))

    return abs(x) + abs(y), first_revisited_distance


if __name__ == '__main__':
    instructions = Path(__file__).with_name('input.txt').read_text().strip()
    part1, part2 = solve(instructions)
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2 if part2 is not None else "no location visited twice"}')
