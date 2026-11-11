from pathlib import Path


def solve(lines: list[str], target: int = 150) -> tuple[int, int]:
    counts = [0] * (target + 1)
    ways_by_size = [[0] * (len(lines) + 1) for _ in range(target + 1)]
    counts[0] = 1
    ways_by_size[0][0] = 1
    for size in map(int, lines):
        for volume in range(target, size - 1, -1):
            counts[volume] += counts[volume - size]
            for used in range(len(lines), 0, -1):
                ways_by_size[volume][used] += ways_by_size[volume - size][used - 1]
    min_used = next((i for i, count in enumerate(ways_by_size[target]) if count), 0)
    return counts[target], ways_by_size[target][min_used]


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
