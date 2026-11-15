from collections import defaultdict, deque
from pathlib import Path


def graph_from(data: str) -> dict[int, set[int]]:
    graph: dict[int, set[int]] = defaultdict(set)
    for line in data.splitlines():
        if line.strip():
            source, destinations = line.split(" <-> ")
            graph[int(source)].update(map(int, destinations.split(", ")))
    return graph


def component(start: int, graph: dict[int, set[int]]) -> set[int]:
    found = {start}
    queue = deque([start])
    while queue:
        for neighbor in graph[queue.popleft()] - found:
            found.add(neighbor)
            queue.append(neighbor)
    return found


def part1(data: str) -> int:
    graph = graph_from(data)
    return len(component(0, graph))


def part2(data: str) -> int:
    graph = graph_from(data)
    remaining = set(graph)
    groups = 0
    while remaining:
        remaining -= component(next(iter(remaining)), graph)
        groups += 1
    return groups


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
