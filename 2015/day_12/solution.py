import json
from pathlib import Path


def sum_numbers(value, ignore_red_objects: bool = False) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, list):
        return sum(sum_numbers(item, ignore_red_objects) for item in value)
    if isinstance(value, dict):
        if ignore_red_objects and 'red' in value.values():
            return 0
        return sum(sum_numbers(item, ignore_red_objects) for item in value.values())
    return 0


def solve(document: str) -> tuple[int, int]:
    data = json.loads(document)
    return sum_numbers(data), sum_numbers(data, ignore_red_objects=True)


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text()), sep='\n')
