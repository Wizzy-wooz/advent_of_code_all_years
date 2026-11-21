from pathlib import Path


def part1(data: str) -> int:
    from collections import defaultdict, deque

    graph = defaultdict(set)
    for line in data.splitlines():
        source, neighbors = line.split(": ")
        for neighbor in neighbors.split():
            graph[source].add(neighbor)
            graph[neighbor].add(source)

    # The puzzle guarantees a minimum cut of three. Four disjoint paths
    # rule out a target; a failed fourth search exposes the two components.
    source = next(iter(graph))
    for target in graph:
        if target == source:
            continue
        residual = {u: {v: 1 for v in neighbors} for u, neighbors in graph.items()}
        for flow in range(4):
            parent = {source: None}
            queue = deque([source])
            while queue and target not in parent:
                node = queue.popleft()
                for neighbor, capacity in residual[node].items():
                    if capacity and neighbor not in parent:
                        parent[neighbor] = node
                        queue.append(neighbor)
            if target not in parent:
                if flow == 3:
                    return len(parent) * (len(graph) - len(parent))
                raise ValueError("Graph has a cut smaller than three")
            node = target
            while node != source:
                previous = parent[node]
                residual[previous][node] -= 1
                residual[node][previous] += 1
                node = previous
    raise ValueError("No three-edge cut found")


def part2(data: str) -> str:
    return "Merry Christmas!"


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
