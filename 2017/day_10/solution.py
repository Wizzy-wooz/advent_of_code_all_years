from pathlib import Path

SUFFIX = [17, 31, 73, 47, 23]


def knot_hash(lengths: list[int], size: int = 256, rounds: int = 1) -> list[int]:
    values = list(range(size))
    position = skip = 0
    for _ in range(rounds):
        for length in lengths:
            if not 0 <= length <= size:
                raise ValueError(f"Invalid knot length: {length}")
            for offset in range(length // 2):
                left = (position + offset) % size
                right = (position + length - offset - 1) % size
                values[left], values[right] = values[right], values[left]
            position = (position + length + skip) % size
            skip += 1
    return values


def dense_hash(data: str) -> str:
    sparse = knot_hash([*data.encode("utf-8"), *SUFFIX], rounds=64)
    dense = [__import__("functools").reduce(int.__xor__, sparse[i:i + 16]) for i in range(0, 256, 16)]
    return "".join(f"{value:02x}" for value in dense)


def part1(data: str) -> int:
    lengths = [int(value) for value in data.strip().split(",") if value.strip()]
    values = knot_hash(lengths)
    return values[0] * values[1]


def part2(data: str) -> str:
    return dense_hash(data.strip())


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
