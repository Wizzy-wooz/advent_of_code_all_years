import ast
from pathlib import Path


def solve(lines: list[str]) -> tuple[int, int]:
    code_chars = memory_chars = encoded_chars = 0
    for literal in lines:
        code_chars += len(literal)
        memory_chars += len(ast.literal_eval(literal))
        encoded_chars += len(literal) + literal.count('\\') + literal.count('"') + 2
    return code_chars - memory_chars, encoded_chars - code_chars


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
