from collections import deque
from pathlib import Path


def battle(data: str, elf_attack: int = 3, no_elf_deaths: bool = False) -> tuple[int, int, bool]:
    grid = [list(row) for row in data.splitlines()];
    units = {};
    uid = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char in "EG": units[uid] = [char, x, y, 200, elf_attack if char == "E" else 3]; grid[y][
                x] = "."; uid += 1

    def neighbors(x, y):
        return [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]

    rounds = 0
    while True:
        order = sorted((u[2], u[1], i) for i, u in units.items())
        for _, _, i in order:
            if i not in units: continue
            faction, x, y, hp, attack = units[i]
            enemies = [u for u in units.values() if u[0] != faction]
            if not enemies: return rounds * sum(u[3] for u in units.values()), rounds, True
            targets = {(tx, ty) for e in enemies for tx, ty in neighbors(e[1], e[2]) if grid[ty][tx] == "."}
            if (x, y) not in targets:
                occupied = {(u[1], u[2]) for u in units.values()};
                occupied.discard((x, y))
                queue = deque([((x, y), 0, None)]);
                seen = {(x, y)};
                candidates = []
                while queue:
                    (cx, cy), dist, first = queue.popleft()
                    if candidates and dist > candidates[0][0]: break
                    if (cx, cy) in targets: candidates.append((dist, cy, cx, first)); continue
                    for nx, ny in neighbors(cx, cy):
                        if (nx, ny) not in seen and (nx, ny) not in occupied and grid[ny][nx] == ".":
                            seen.add((nx, ny));
                            queue.append(((nx, ny), dist + 1, first or (nx, ny)))
                if candidates:
                    _, _, _, (x, y) = min(candidates)
                    units[i][1:3] = [x, y]
            adjacent = [j for j, e in units.items() if e[0] != faction and (e[1], e[2]) in neighbors(x, y)]
            if adjacent:
                target = min(adjacent, key=lambda j: (units[j][3], units[j][2], units[j][1]))
                units[target][3] -= attack
                if units[target][3] <= 0:
                    dead = units.pop(target)
                    if no_elf_deaths and dead[0] == "E": return 0, rounds, False
        rounds += 1


def part1(data: str) -> int: return battle(data)[0]


def part2(data: str) -> int:
    for attack in range(4, 201):
        result, _, success = battle(data, attack, True)
        if success: return result
    raise ValueError("No elf victory found")


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
