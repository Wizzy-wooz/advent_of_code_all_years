import re
from pathlib import Path


def solve(lines: list[str], teaspoons: int = 100) -> tuple[int, int]:
    ingredients = []
    for line in lines:
        numbers = list(map(int, re.findall(r'-?\d+', line)))
        ingredients.append(numbers)
    best = best_500 = 0

    def search(index: int, remaining: int, amounts: list[int]) -> None:
        nonlocal best, best_500
        if index == len(ingredients) - 1:
            allocation = amounts + [remaining]
            totals = [sum(allocation[i] * ingredients[i][j] for i in range(len(ingredients)))
                      for j in range(5)]
            score = 1
            for value in totals[:4]:
                score *= max(0, value)
            best = max(best, score)
            if totals[4] == 500:
                best_500 = max(best_500, score)
            return
        for amount in range(remaining + 1):
            search(index + 1, remaining - amount, amounts + [amount])

    if ingredients:
        search(0, teaspoons, [])
    return best, best_500


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
