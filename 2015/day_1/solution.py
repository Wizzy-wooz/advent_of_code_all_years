from pathlib import Path


def part1(instructions: str) -> int:
    return instructions.count('(') - instructions.count(')')


def part2(instructions: str) -> int:
    floor = 0
    for position, instruction in enumerate(instructions, start=1):
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1

        if floor == -1:
            return position

    raise ValueError("Santa never enters the basement")


if __name__ == '__main__':
    instructions = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2(instructions)}')

