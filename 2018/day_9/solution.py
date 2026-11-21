from pathlib import Path
import re


def high_score(players: int, last_marble: int) -> int:
    next_marble = [0] * (last_marble + 1);
    prev_marble = [0] * (last_marble + 1)
    scores = [0] * players;
    current = 0
    for marble in range(1, last_marble + 1):
        player = (marble - 1) % players
        if marble % 23:
            left = next_marble[current];
            right = next_marble[left]
            next_marble[left] = marble;
            prev_marble[marble] = left
            next_marble[marble] = right;
            prev_marble[right] = marble;
            current = marble
        else:
            scores[player] += marble
            for _ in range(7): current = prev_marble[current]
            scores[player] += current
            left, right = prev_marble[current], next_marble[current]
            next_marble[left] = right;
            prev_marble[right] = left;
            current = right
    return max(scores)


def parse(data: str) -> tuple[int, int]:
    values = list(map(int, re.findall(r"\d+", data)))
    if len(values) < 2: raise ValueError("Expected player count and final marble")
    return values[0], values[1]


def part1(data: str) -> int:
    players, last = parse(data);
    return high_score(players, last)


def part2(data: str) -> int:
    players, last = parse(data);
    return high_score(players, last * 100)


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
