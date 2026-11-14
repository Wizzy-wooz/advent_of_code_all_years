def find_sum(digits):
    if not digits:
        return 0

    return sum(
        digit
        for i, digit in enumerate(digits)
        if digit == digits[(i + 1) % len(digits)]
    )


def find_sum_halfway(digits):
    if not digits:
        return 0

    halfway = len(digits) // 2
    return sum(
        digit
        for i, digit in enumerate(digits)
        if digit == digits[(i + halfway) % len(digits)]
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        digits = [int(c) for c in f.read().strip()]

    print("Part 1:", find_sum(digits))
    print("Part 2:", find_sum_halfway(digits))
