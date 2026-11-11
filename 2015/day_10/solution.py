from pathlib import Path


def look_and_say(seed: str, rounds: int) -> int:
    value = seed
    for _ in range(rounds):
        parts = []
        i = 0
        while i < len(value):
            j = i + 1
            while j < len(value) and value[j] == value[i]:
                j += 1
            parts.extend((str(j - i), value[i]))
            i = j
        value = ''.join(parts)
    return len(value)


def solve(seed: str) -> tuple[int, int]:
    return look_and_say(seed, 40), look_and_say(seed, 50)


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().strip()), sep='\n')
