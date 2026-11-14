from functools import lru_cache
from hashlib import md5
import re


def key_index(salt: str, stretched: bool = False) -> int:
    @lru_cache(None)
    def digest(i):
        value = md5(f'{salt}{i}'.encode()).hexdigest()
        if stretched:
            for _ in range(2016): value = md5(value.encode()).hexdigest()
        return value
    found = []; i = 0
    while len(found) < 64:
        h = digest(i); trip = re.search(r'(.)\1\1', h)
        if trip and any(re.search(re.escape(trip[1]) + '{5}', digest(j)) for j in range(i+1, i+1001)):
            found.append(i)
        i += 1
    return found[-1]


def part1(data: str) -> int: return key_index(data.strip())
def part2(data: str) -> int: return key_index(data.strip(), True)


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
