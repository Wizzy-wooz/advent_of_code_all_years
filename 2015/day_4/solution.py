import hashlib
from pathlib import Path


def mine(secret_key: str, zeroes: int) -> int:
    prefix = '0' * zeroes
    number = 1
    while True:
        digest = hashlib.md5(f'{secret_key}{number}'.encode()).hexdigest()
        if digest.startswith(prefix):
            return number
        number += 1


def mine_advent_coins(secret_key: str) -> tuple[int, int]:
    five_zeroes = None
    number = 1
    while True:
        digest = hashlib.md5(f'{secret_key}{number}'.encode()).hexdigest()
        if five_zeroes is None and digest.startswith('00000'):
            five_zeroes = number
        if digest.startswith('000000'):
            return five_zeroes, number
        number += 1


def part1(secret_key: str) -> int:
    return mine(secret_key, 5)


def part2(secret_key: str) -> int:
    return mine(secret_key, 6)


if __name__ == '__main__':
    secret_key = Path(__file__).with_name('input.txt').read_text().strip()
    part1_answer, part2_answer = mine_advent_coins(secret_key)
    print(f'Part 1: {part1_answer}')
    print(f'Part 2: {part2_answer}')
