import re
from pathlib import Path


TARGET = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
          'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3,
          'cars': 2, 'perfumes': 1}


def solve(lines: list[str]) -> tuple[int | None, int | None]:
    exact = ranged = None
    for line in lines:
        m = re.match(r'Sue (\d+): (.*)', line)
        if not m:
            continue
        number, props = int(m.group(1)), dict((key, int(value)) for key, value in
                                               re.findall(r'(\w+): (\d+)', m.group(2)))
        if all(TARGET[key] == value for key, value in props.items()):
            exact = number
        if all((value > TARGET[key] if key in ('cats', 'trees') else
                value < TARGET[key] if key in ('pomeranians', 'goldfish') else
                value == TARGET[key]) for key, value in props.items()):
            ranged = number
    return exact, ranged


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
