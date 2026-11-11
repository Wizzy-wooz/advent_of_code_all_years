from functools import lru_cache
from itertools import combinations
from math import prod
from pathlib import Path


def best_quantum_entanglement(weights: list[int], groups: int) -> int:
    if sum(weights) % groups:
        raise ValueError('Package weights cannot be split into equal totals')
    target = sum(weights) // groups
    indexed = tuple(sorted(weights, reverse=True))

    @lru_cache(None)
    def can_split(mask: int, groups_left: int) -> bool:
        if groups_left == 1:
            return sum(indexed[i] for i in range(len(indexed)) if mask >> i & 1) == target
        first = (mask & -mask).bit_length() - 1
        rest = [i for i in range(first + 1, len(indexed)) if mask >> i & 1]
        required = target - indexed[first]
        for size in range(len(rest) + 1):
            for subset in combinations(rest, size):
                if sum(indexed[i] for i in subset) == required:
                    group_mask = (1 << first) | sum(1 << i for i in subset)
                    if can_split(mask ^ group_mask, groups_left - 1):
                        return True
        return False

    full_mask = (1 << len(indexed)) - 1
    for count in range(1, len(indexed) + 1):
        candidates = []
        for chosen_indices in combinations(range(len(indexed)), count):
            chosen = [indexed[i] for i in chosen_indices]
            if sum(chosen) == target:
                chosen_mask = sum(1 << i for i in chosen_indices)
                if can_split(full_mask ^ chosen_mask, groups - 1):
                    candidates.append(prod(chosen))
        if candidates:
            return min(candidates)
    raise ValueError('Could not divide packages into equal-weight groups')


def solve(lines: list[str]) -> tuple[int, int]:
    try:
        weights = [int(line) for line in lines if line.strip()]
    except ValueError as error:
        raise ValueError('Day 24 input must contain one package weight per line') from error
    return best_quantum_entanglement(weights, 3), best_quantum_entanglement(weights, 4)


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
