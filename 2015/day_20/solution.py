from pathlib import Path


def first_house(target: int, presents_per_visit: int, visit_limit: int | None = None) -> int:
    limit = 1
    while True:
        presents = [0] * (limit + 1)
        for elf in range(1, limit + 1):
            final = min(limit, elf * visit_limit) if visit_limit else limit
            for house in range(elf, final + 1, elf):
                presents[house] += elf * presents_per_visit
        for house in range(1, limit + 1):
            if presents[house] >= target:
                return house
        limit *= 2


def solve(target: int) -> tuple[int, int]:
    return first_house(target, 10), first_house(target, 11, 50)


if __name__ == '__main__':
    target = int(Path(__file__).with_name('input.txt').read_text().strip())
    print(*solve(target), sep='\n')
