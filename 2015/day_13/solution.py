from itertools import permutations
from pathlib import Path


def max_happiness(happiness: dict[tuple[str, str], int], people: set[str]) -> int:
    first = min(people)
    others = people - {first}
    best = float('-inf')
    for rest in permutations(others):
        order = (first, *rest)
        total = sum(happiness[a, b] + happiness[b, a]
                    for a, b in zip(order, order[1:] + order[:1]))
        best = max(best, total)
    return int(best)


def solve(lines: list[str]) -> tuple[int, int]:
    happiness = {}
    people = set()
    for line in lines:
        if not line.strip():
            continue
        words = line.rstrip('.').split()
        a, sign, amount, b = words[0], words[2], int(words[3]), words[-1]
        happiness[a, b] = amount if sign == 'gain' else -amount
        people.update((a, b))
    first = max_happiness(happiness, people)
    for person in people:
        happiness['Me', person] = happiness[person, 'Me'] = 0
    return first, max_happiness(happiness, people | {'Me'})


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
