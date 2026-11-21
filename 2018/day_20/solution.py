from collections import defaultdict, deque
from pathlib import Path

DELTAS = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}


def distances(data: str) -> dict[tuple[int, int], int]:
    expression = data.strip().removeprefix("^").removesuffix("$")
    graph = defaultdict(set);
    current = {(0, 0)};
    stack = []
    for char in expression:
        if char in DELTAS:
            dx, dy = DELTAS[char];
            following = set()
            for x, y in current:
                neighbor = (x + dx, y + dy);
                graph[(x, y)].add(neighbor);
                graph[neighbor].add((x, y));
                following.add(neighbor)
            current = following
        elif char == "(":
            stack.append((set(current), set()))
        elif char == "|":
            start, ends = stack[-1]; ends.update(current); current = set(start)
        elif char == ")":
            start, ends = stack.pop();
            ends.update(current);
            current = ends
    result = {(0, 0): 0};
    queue = deque([(0, 0)])
    while queue:
        room = queue.popleft()
        for neighbor in graph[room]:
            if neighbor not in result: result[neighbor] = result[room] + 1; queue.append(neighbor)
    return result


def part1(data: str) -> int: return max(distances(data).values(), default=0)


def part2(data: str) -> int: return sum(value >= 1000 for value in distances(data).values())


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
