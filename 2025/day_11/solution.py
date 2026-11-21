from functools import lru_cache
from pathlib import Path


def parse(data: str) -> dict[str, tuple[str, ...]]:
    graph = {}
    for line in data.splitlines():
        if line.strip():
            device, outputs = line.split(": ")
            graph[device] = tuple(outputs.split())
    return graph


def count_paths(data: str, start: str, required: tuple[str, ...] = ()) -> int:
    graph = parse(data)
    required_bits = {device: 1 << i for i, device in enumerate(required)}
    complete = (1 << len(required)) - 1
    active = set()

    @lru_cache(None)
    def visit(device: str, mask: int) -> int:
        mask |= required_bits.get(device, 0)
        if device == "out":
            return int(mask == complete)

        state = (device, mask)
        if state in active:
            raise ValueError("The device graph contains a cycle, so path count is unbounded")
        active.add(state)
        total = sum(visit(output, mask) for output in graph.get(device, ()))
        active.remove(state)
        return total

    return visit(start, 0)


def part1(data: str) -> int:
    return count_paths(data, "you")


def part2(data: str) -> int:
    return count_paths(data, "svr", ("dac", "fft"))


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
