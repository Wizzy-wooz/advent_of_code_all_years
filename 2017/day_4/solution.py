from pathlib import Path


def is_valid_passphrase(words: list[str]) -> bool:
    return len(words) == len(set(words))


def is_valid_no_anagrams(words: list[str]) -> bool:
    normalized = ["".join(sorted(word)) for word in words]
    return len(normalized) == len(set(normalized))


def part1(data: str) -> int:
    return sum(
        is_valid_passphrase(line.split())
        for line in data.splitlines()
        if line.strip()
    )


def part2(data: str) -> int:
    return sum(
        is_valid_no_anagrams(line.split())
        for line in data.splitlines()
        if line.strip()
    )


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
