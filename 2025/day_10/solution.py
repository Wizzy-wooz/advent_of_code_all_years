from collections import deque
from fractions import Fraction
from math import ceil
from pathlib import Path
import re


def machines(data: str):
    for line in data.splitlines():
        if not line.strip():
            continue
        lights = re.search(r"\[([.#]+)\]", line)[1]
        buttons = [tuple(map(int, match.split(","))) for match in re.findall(r"\(([^)]+)\)", line)]
        joltage = tuple(map(int, re.search(r"\{([^}]+)\}", line)[1].split(",")))
        yield lights, buttons, joltage


def light_presses(lights: str, buttons: list[tuple[int, ...]]) -> int:
    target = sum(1 << i for i, char in enumerate(lights) if char == "#")
    masks = [sum(1 << i for i in button) for button in buttons]
    queue = deque([(0, 0)])
    seen = {0}
    while queue:
        state, presses = queue.popleft()
        if state == target:
            return presses
        for mask in masks:
            following = state ^ mask
            if following not in seen:
                seen.add(following)
                queue.append((following, presses + 1))
    raise ValueError("The light configuration cannot be reached")


def joltage_presses(buttons: list[tuple[int, ...]], target: tuple[int, ...]) -> int:
    button_sets = tuple(frozenset(button) for button in buttons)
    button_count = len(button_sets)
    limits = [min(target[j] for j in button) for button in button_sets]

    # Solve A*x = target over the rationals, expressing pivot button counts
    # in terms of the free button counts. The input machines have at most a
    # few free variables, so this avoids exploring every press-count tuple.
    matrix = [
        [Fraction(int(counter in button)) for button in button_sets] + [Fraction(target[row])]
        for row, counter in enumerate(range(len(target)))
    ]
    pivot_columns = []
    pivot_row = 0
    for column in range(button_count):
        selected = next((r for r in range(pivot_row, len(matrix)) if matrix[r][column]), None)
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        divisor = matrix[pivot_row][column]
        matrix[pivot_row] = [value / divisor for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row != pivot_row and matrix[row][column]:
                factor = matrix[row][column]
                matrix[row] = [a - factor * b for a, b in zip(matrix[row], matrix[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(matrix):
            break

    for row in matrix:
        if not any(row[:button_count]) and row[-1]:
            raise ValueError("The joltage target cannot be reached")

    free_columns = [column for column in range(button_count) if column not in pivot_columns]
    free_bounds = {column: limits[column] for column in free_columns}
    pivot_expressions = {}
    for row_index, column in enumerate(pivot_columns):
        row = matrix[row_index]
        pivot_expressions[column] = (row[-1], {free: -row[free] for free in free_columns})

    def evaluated_values(free_values):
        result = [Fraction(0)] * button_count
        for column, value in free_values.items():
            result[column] = Fraction(value)
        for column, (constant, coefficients) in pivot_expressions.items():
            result[column] = constant + sum(coefficients[c] * free_values[c] for c in free_columns)
        return result

    best = sum(target) + 1
    best_assignment = None
    order = sorted(
        free_columns,
        key=lambda column: (
            free_bounds[column],
            -sum(abs(coefficients.get(column, 0)) for _, coefficients in pivot_expressions.values()),
        ),
    )
    free_values = {}

    def search(index: int):
        nonlocal best, best_assignment
        objective_constant = sum(constant for constant, _ in pivot_expressions.values())
        objective_coefficients = {
            column: Fraction(1) + sum(coefficients[column] for _, coefficients in pivot_expressions.values())
            for column in free_columns
        }
        lower_bound = Fraction(objective_constant)
        for column in free_columns:
            coefficient = objective_coefficients[column]
            if column in free_values:
                lower_bound += coefficient * free_values[column]
            elif coefficient < 0:
                lower_bound += coefficient * free_bounds[column]
        if ceil(lower_bound) >= best:
            return

        # Reject a partial assignment if any pivot button can no longer fit
        # within its nonnegative integer press-count bounds.
        for column, (constant, coefficients) in pivot_expressions.items():
            low = high = constant
            for free in free_columns:
                coefficient = coefficients[free]
                if free in free_values:
                    low += coefficient * free_values[free]
                    high += coefficient * free_values[free]
                elif coefficient < 0:
                    low += coefficient * free_bounds[free]
                else:
                    high += coefficient * free_bounds[free]
            if high < 0 or low > limits[column]:
                return

        if index == len(order):
            values = evaluated_values(free_values)
            if all(value.denominator == 1 and 0 <= value <= limits[i] for i, value in enumerate(values)):
                total = sum(int(value) for value in values)
                if total < best:
                    best = total
                    best_assignment = values
            return

        column = order[index]
        for value in range(free_bounds[column] + 1):
            free_values[column] = value
            search(index + 1)
        del free_values[column]

    search(0)
    if best_assignment is None:
        raise ValueError("The joltage target cannot be reached")
    return best


def solve(data: str) -> tuple[int, int]:
    light_total = joltage_total = 0
    for lights, buttons, target in machines(data):
        light_total += light_presses(lights, buttons)
        joltage_total += joltage_presses(buttons, target)
    return light_total, joltage_total


def part1(data: str) -> int:
    return solve(data)[0]


def part2(data: str) -> int:
    return solve(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
