from pathlib import Path


def traverse(data: str) -> tuple[str, int]:
    grid = data.splitlines()
    if not grid:
        return "", 0

    def at(x: int, y: int) -> str:
        if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
            return grid[y][x]
        return " "

    x = grid[0].find("|")
    if x < 0:
        raise ValueError("The diagram has no starting path")

    y, dx, dy = 0, 0, 1
    letters: list[str] = []
    steps = 0
    visited: set[tuple[int, int, int, int]] = set()

    while at(x, y) != " ":
        state = (x, y, dx, dy)
        if state in visited:
            raise ValueError("The diagram contains a loop")
        visited.add(state)

        char = at(x, y)
        steps += 1
        if char.isalpha():
            letters.append(char)

        if char == "+":
            # At a junction, turn left or right relative to the direction of travel.
            turns = ((-dy, dx), (dy, -dx))
            possible = [(ndx, ndy) for ndx, ndy in turns if at(x + ndx, y + ndy) != " "]
            if not possible:
                break
            dx, dy = possible[0]

        x += dx
        y += dy

    return "".join(letters), steps


def part1(data: str) -> str:
    return traverse(data)[0]


def part2(data: str) -> int:
    return traverse(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
