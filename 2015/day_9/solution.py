from itertools import permutations
from pathlib import Path


def solve(lines: list[str]) -> tuple[int, int]:
    distances = {}
    cities = set()
    for line in lines:
        if not line.strip():
            continue
        left, _, right, _, distance = line.split()
        distances[left, right] = distances[right, left] = int(distance)
        cities.update((left, right))
    routes = (sum(distances[a, b] for a, b in zip(route, route[1:]))
              for route in permutations(cities))
    routes = list(routes)
    return min(routes), max(routes)


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
