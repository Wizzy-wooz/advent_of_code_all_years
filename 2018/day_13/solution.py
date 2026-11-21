from pathlib import Path


def run(data: str, stop_at_first_crash: bool = False) -> tuple[str | None, str | None]:
    rows = data.splitlines();
    tracks = [list(row) for row in rows];
    carts = {}
    for y, row in enumerate(tracks):
        for x, char in enumerate(row):
            if char in "^v<>": carts[(x, y)] = [char, 0]; tracks[y][x] = "|" if char in "^v" else "-"
    directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
    turn_left = {"^": "<", "<": "v", "v": ">", ">": "^"}
    turn_right = {v: k for k, v in turn_left.items()}
    first_crash = None
    while len(carts) > 1:
        moved = set()
        for x, y in sorted(carts, key=lambda p: (p[1], p[0])):
            if (x, y) not in carts: continue
            direction, turn = carts.pop((x, y));
            dx, dy = directions[direction];
            nx, ny = x + dx, y + dy
            if (nx, ny) in carts or (nx, ny) in moved:
                carts.pop((nx, ny), None);
                moved.discard((nx, ny))
                if first_crash is None:
                    first_crash = f"{nx},{ny}"
                    if stop_at_first_crash: return first_crash, None
                continue
            track = tracks[ny][nx]
            if track == "/":
                direction = {"^": ">", "v": "<", "<": "v", ">": "^"}[direction]
            elif track == "\\":
                direction = {"^": "<", "v": ">", "<": "^", ">": "v"}[direction]
            elif track == "+":
                if turn == 0:
                    direction = turn_left[direction]
                elif turn == 2:
                    direction = turn_right[direction]
                turn = (turn + 1) % 3
            carts[(nx, ny)] = [direction, turn];
            moved.add((nx, ny))
    last = next(iter(carts), None)
    return first_crash, f"{last[0]},{last[1]}" if last is not None else None


def part1(data: str) -> str:
    crash, _ = run(data, stop_at_first_crash=True)
    if crash is None: raise ValueError("No cart collision occurred")
    return crash


def part2(data: str) -> str:
    _, last = run(data)
    if last is None: raise ValueError("All carts crashed")
    return last


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
