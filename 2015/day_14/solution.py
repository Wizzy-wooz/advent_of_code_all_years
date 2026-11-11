import re
from pathlib import Path


def solve(lines: list[str], duration: int = 2503) -> tuple[int, int]:
    reindeer = []
    for line in lines:
        m = re.fullmatch(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.', line)
        if m:
            name, speed, fly, rest = m.groups()
            reindeer.append((name, int(speed), int(fly), int(rest)))
    distances = {name: 0 for name, *_ in reindeer}
    points = distances.copy()
    for second in range(1, duration + 1):
        for name, speed, fly, rest in reindeer:
            if (second - 1) % (fly + rest) < fly:
                distances[name] += speed
        lead = max(distances.values())
        for name, distance in distances.items():
            if distance == lead:
                points[name] += 1
    return max(distances.values()), max(points.values())


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
