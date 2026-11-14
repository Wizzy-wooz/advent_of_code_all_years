from itertools import combinations
from pathlib import Path


def checksum(rows):
    return sum(max(row) - min(row) for row in rows)


def divisible_checksum(rows):
    total = 0

    for row in rows:
        for a, b in combinations(row, 2):
            if a % b == 0:
                total += a // b
                break
            if b % a == 0:
                total += b // a
                break
        else:
            raise ValueError(f"No evenly divisible pair found in row: {row}")

    return total


if __name__ == "__main__":
    input_path = Path(__file__).with_name("input.txt")
    rows = [
        [int(value) for value in line.split()]
        for line in input_path.read_text().splitlines()
        if line.strip()
    ]

    print("Part 1:", checksum(rows))
    print("Part 2:", divisible_checksum(rows))
