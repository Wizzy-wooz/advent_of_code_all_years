import re
from pathlib import Path


def code_at(row: int, column: int) -> int:
    diagonal = row + column - 1
    index = diagonal * (diagonal - 1) // 2 + column
    return 20151125 * pow(252533, index - 1, 33554393) % 33554393


def solve(text: str) -> int:
    row, column = map(int, re.findall(r'row (\d+), column (\d+)', text)[0])
    return code_at(row, column)


if __name__ == '__main__':
    print(solve(Path(__file__).with_name('input.txt').read_text()))
