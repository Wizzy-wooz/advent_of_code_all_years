from collections import Counter
from pathlib import Path
import re


LINE_PATTERN = re.compile(r"^(\w+) \((\d+)\)(?: -> (.*))?$")


def parse_programs(data: str) -> tuple[dict[str, int], dict[str, list[str]]]:
    weights: dict[str, int] = {}
    children: dict[str, list[str]] = {}

    for line in data.splitlines():
        match = LINE_PATTERN.match(line.strip())
        if not match:
            if line.strip():
                raise ValueError(f"Invalid program description: {line}")
            continue
        name, weight, child_list = match.groups()
        weights[name] = int(weight)
        children[name] = child_list.split(", ") if child_list else []

    return weights, children


def find_root(children: dict[str, list[str]]) -> str:
    all_children = {child for names in children.values() for child in names}
    roots = set(children) - all_children
    if len(roots) != 1:
        raise ValueError(f"Expected one root program, found {len(roots)}")
    return roots.pop()


def corrected_weight(data: str) -> int:
    weights, children = parse_programs(data)
    root = find_root(children)

    def total_weight(name: str) -> tuple[int, int | None]:
        child_totals = [total_weight(child) for child in children[name]]
        for total, correction in child_totals:
            if correction is not None:
                return 0, correction

        totals = [total for total, _ in child_totals]
        counts = Counter(totals)
        if len(counts) > 1:
            expected, _ = counts.most_common(1)[0]
            wrong = next(value for value, count in counts.items() if count == 1)
            wrong_child = children[name][totals.index(wrong)]
            return 0, weights[wrong_child] + expected - wrong

        return weights[name] + sum(totals), None

    _, correction = total_weight(root)
    if correction is None:
        raise ValueError("All programs are already balanced")
    return correction


def part1(data: str) -> str:
    return find_root(parse_programs(data)[1])


def part2(data: str) -> int:
    return corrected_weight(data)


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
