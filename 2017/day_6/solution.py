from pathlib import Path


def redistribute(banks: list[int]) -> list[int]:
    if not banks:
        raise ValueError("At least one memory bank is required")

    result = banks.copy()
    index = result.index(max(result))
    blocks = result[index]
    result[index] = 0

    for step in range(1, blocks + 1):
        result[(index + step) % len(result)] += 1

    return result


def cycle_info(banks: list[int]) -> tuple[int, int]:
    seen: dict[tuple[int, ...], int] = {}
    state = banks.copy()
    cycles = 0

    while tuple(state) not in seen:
        seen[tuple(state)] = cycles
        state = redistribute(state)
        cycles += 1

    loop_size = cycles - seen[tuple(state)]
    return cycles, loop_size


def part1(data: str) -> int:
    banks = [int(value) for value in data.split()]
    return cycle_info(banks)[0]


def part2(data: str) -> int:
    banks = [int(value) for value in data.split()]
    return cycle_info(banks)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
