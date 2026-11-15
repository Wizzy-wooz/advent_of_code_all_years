from functools import lru_cache
from pathlib import Path

def parse(data: str) -> tuple[tuple[int, int], ...]:
    return tuple(tuple(map(int, line.split("/"))) for line in data.splitlines() if line.strip())

def bridge_scores(data: str) -> tuple[int, int]:
    components = parse(data)
    @lru_cache(None)
    def search(port: int, used: int) -> tuple[int, int, int]:
        strongest = longest_length = longest_strength = 0
        for i, (a, b) in enumerate(components):
            if used >> i & 1 or (a != port and b != port):
                continue
            next_port = b if a == port else a
            strength, length, long_strength = search(next_port, used | (1 << i))
            strength += a + b
            length += 1
            long_strength += a + b
            strongest = max(strongest, strength)
            if length > longest_length or (length == longest_length and long_strength > longest_strength):
                longest_length, longest_strength = length, long_strength
        return strongest, longest_length, longest_strength
    strongest, _, longest_strength = search(0, 0)
    return strongest, longest_strength

def part1(data: str) -> int: return bridge_scores(data)[0]
def part2(data: str) -> int: return bridge_scores(data)[1]

if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
