from pathlib import Path


def dance(data: str, count: int = 1, size: int = 16) -> str:
    moves = data.strip().split(",")
    programs = [chr(ord("a") + i) for i in range(size)]
    seen: dict[str, int] = {}
    iteration = 0
    while iteration < count:
        state = "".join(programs)
        if state in seen:
            cycle = iteration - seen[state]
            count = iteration + (count - iteration) % cycle
        else:
            seen[state] = iteration
        for move in moves:
            if move[0] == "s":
                amount = int(move[1:])
                programs = programs[-amount:] + programs[:-amount]
            elif move[0] == "x":
                a, b = map(int, move[1:].split("/"))
                programs[a], programs[b] = programs[b], programs[a]
            elif move[0] == "p":
                a, b = move[1:].split("/")
                ia, ib = programs.index(a), programs.index(b)
                programs[ia], programs[ib] = programs[ib], programs[ia]
        iteration += 1
    return "".join(programs)


def part1(data: str) -> str:
    return dance(data)


def part2(data: str) -> str:
    return dance(data, 1_000_000_000)


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
