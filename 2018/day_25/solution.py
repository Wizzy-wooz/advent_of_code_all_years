from pathlib import Path


def part1(data: str) -> int:
    points = [tuple(map(int, line.split(","))) for line in data.splitlines() if line.strip()]
    parent = list(range(len(points)))

    def find(a):
        while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
        return a

    for i, p in enumerate(points):
        for j in range(i):
            if sum(abs(p[k] - points[j][k]) for k in range(4)) <= 3:
                a, b = find(i), find(j)
                if a != b: parent[a] = b
    return len({find(i) for i in range(len(points))})


def part2(data: str) -> str: return "Merry Christmas!"


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
