from pathlib import Path


def part1(data: str) -> int:
    graph = {}
    for line in data.splitlines():
        if not line.strip():
            continue
        source, destinations = line.split(": ")
        graph.setdefault(source, {})
        for target in destinations.split():
            graph.setdefault(target, {})
            graph[source][target] = graph[source].get(target, 0) + 1
            graph[target][source] = graph[target].get(source, 0) + 1

    groups = {node: {node} for node in graph}
    nodes = list(graph)
    total = len(nodes)
    best_cut = float("inf")
    best_size = 0
    while len(nodes) > 1:
        used = set()
        weights = {node: 0 for node in nodes}
        previous = None
        for index in range(len(nodes)):
            selected = max((node for node in nodes if node not in used), key=lambda node: weights[node])
            used.add(selected)
            if index == len(nodes) - 1:
                if weights[selected] < best_cut:
                    best_cut = weights[selected]
                    best_size = len(groups[selected])
                for node in nodes:
                    if node != selected and node != previous:
                        weight = graph[selected].get(node, 0)
                        graph[previous][node] = graph[previous].get(node, 0) + weight
                        graph[node][previous] = graph[node].get(previous, 0) + weight
                        graph[node].pop(selected, None)
                graph[previous].pop(selected, None)
                graph.pop(selected)
                groups[previous].update(groups.pop(selected))
                nodes.remove(selected)
                break
            previous = selected
            for node in nodes:
                if node not in used:
                    weights[node] += graph[selected].get(node, 0)
    if best_cut != 3:
        raise ValueError(f"Expected a three-edge minimum cut, found {best_cut}")
    return best_size * (total - best_size)


def part2(data: str) -> str:
    return "Merry Christmas!"


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
