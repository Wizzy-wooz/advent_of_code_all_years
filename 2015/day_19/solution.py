import re
from pathlib import Path


def parse(text: str):
    rules_text, molecule = text.strip().split('\n\n')
    rules = [tuple(line.split(' => ')) for line in rules_text.splitlines()]
    return rules, molecule.strip()


def solve(text: str) -> tuple[int, int]:
    rules, molecule = parse(text)
    generated = set()
    for source, replacement in rules:
        start = 0
        while (index := molecule.find(source, start)) != -1:
            generated.add(molecule[:index] + replacement + molecule[index + len(source):])
            start = index + 1
    tokens = re.findall(r'[A-Z][a-z]?', molecule)
    steps = len(tokens) - tokens.count('Rn') - tokens.count('Ar') - 2 * tokens.count('Y') - 1
    return len(generated), steps


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text()), sep='\n')
