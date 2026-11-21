from pathlib import Path


Instruction = tuple[str, int, int, int]


def parse_program(data: str) -> tuple[int, list[Instruction]]:
    lines = [line.split() for line in data.splitlines() if line.strip()]
    if not lines or len(lines[0]) != 2 or lines[0][0] != "#ip":
        raise ValueError("Program must start with an instruction pointer binding")

    ip_register = int(lines[0][1])
    program = [(op, int(a), int(b), int(c)) for op, a, b, c in lines[1:]]
    return ip_register, program


def halt_values(data: str) -> tuple[int, int]:
    _, program = parse_program(data)
    halt_check = next(
        (
            instruction
            for instruction in program
            if instruction[0] == "eqrr" and 0 in instruction[1:3]
        ),
        None,
    )
    if halt_check is None:
        raise ValueError("Program has no equality check against register 0")

    _, a, b, _ = halt_check
    value_register = b if a == 0 else a

    mix_instruction = next(
        (
            instruction
            for instruction in program
            if instruction[0] == "bori" and instruction[1] == value_register
        ),
        None,
    )
    if mix_instruction is None:
        raise ValueError("Could not find the value mixing instruction")

    _, _, or_value, scratch_register = mix_instruction
    mix_index = program.index(mix_instruction)
    loop_program = program[mix_index + 1 :]

    seed_instruction = next(
        (
            instruction
            for instruction in loop_program
            if instruction[0] == "seti" and instruction[3] == value_register
        ),
        None,
    )
    if seed_instruction is None:
        raise ValueError("Could not find the value seed instruction")
    seed = seed_instruction[1]

    byte_mask = next(
        (
            instruction[2]
            for instruction in loop_program
            if instruction[0] == "bani"
            and instruction[1] == scratch_register
            and instruction[3] != scratch_register
        ),
        None,
    )
    value_mask = next(
        (
            instruction[2]
            for instruction in loop_program
            if instruction[0] == "bani"
            and instruction[1] == value_register
            and instruction[3] == value_register
        ),
        None,
    )
    multiplier = next(
        (
            instruction[2]
            for instruction in loop_program
            if instruction[0] == "muli"
            and instruction[1] == value_register
            and instruction[3] == value_register
        ),
        None,
    )
    divisor = next(
        (
            instruction[1]
            for instruction in loop_program
            if instruction[0] == "gtir" and instruction[2] == scratch_register
        ),
        None,
    )
    if None in (byte_mask, value_mask, multiplier, divisor):
        raise ValueError("Could not extract the value generation constants")

    seen = set()
    value = 0
    first_value = None
    last_value = None

    while True:
        scratch = value | or_value
        value = seed

        while True:
            value = (value + (scratch & byte_mask)) & value_mask
            value = (value * multiplier) & value_mask
            if scratch < divisor:
                break
            scratch //= divisor

        if value in seen:
            return first_value, last_value

        seen.add(value)
        if first_value is None:
            first_value = value
        last_value = value


def part1(data: str) -> int:
    return halt_values(data)[0]


def part2(data: str) -> int:
    return halt_values(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
