from pathlib import Path


def run(data: str) -> tuple[int, int]:
    registers: dict[str, int] = {}
    highest_ever = 0
    for line in data.splitlines():
        if not line.strip():
            continue
        target, operation, amount, _, check, comparator, value = line.split()
        left = registers.get(check, 0)
        right = int(value)
        condition = {
            ">": left > right, "<": left < right, ">=": left >= right,
            "<=": left <= right, "==": left == right, "!=": left != right,
        }[comparator]
        if condition:
            delta = int(amount) * (1 if operation == "inc" else -1)
            registers[target] = registers.get(target, 0) + delta
            highest_ever = max(highest_ever, registers[target])
    return max(registers.values(), default=0), highest_ever


def part1(data: str) -> int:
    return run(data)[0]


def part2(data: str) -> int:
    return run(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
