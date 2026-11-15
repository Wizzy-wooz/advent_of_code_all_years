from pathlib import Path
import re

MODULUS = 2_147_483_647

def seeds(data: str) -> tuple[int, int]:
    values = list(map(int, re.findall(r"\d+", data)))
    if len(values) < 2:
        raise ValueError("Input must contain both generator seeds")
    return values[0], values[1]

def judge(data: str, pairs: int, multiple_a: int = 1, multiple_b: int = 1) -> int:
    a, b = seeds(data)
    matches = 0
    for _ in range(pairs):
        while True:
            a = a * 16_807 % MODULUS
            if a % multiple_a == 0:
                break
        while True:
            b = b * 48_271 % MODULUS
            if b % multiple_b == 0:
                break
        matches += (a & 0xFFFF) == (b & 0xFFFF)
    return matches

def part1(data: str) -> int:
    return judge(data, 40_000_000)

def part2(data: str) -> int:
    return judge(data, 5_000_000, 4, 8)

if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
