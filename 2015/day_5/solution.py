from pathlib import Path


def nice_part1(word: str) -> bool:
    # В строке должно быть не меньше трёх гласных.
    vowels = 'aeiou'
    vowel_count = sum(1 for letter in word if letter in vowels)

    # Проверяем, есть ли две одинаковые буквы подряд.
    has_double_letter = False
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            has_double_letter = True
            break

    # Эти сочетания букв запрещены.
    forbidden_pairs = ('ab', 'cd', 'pq', 'xy')
    has_forbidden_pair = any(pair in word for pair in forbidden_pairs)

    return vowel_count >= 3 and has_double_letter and not has_forbidden_pair


def nice_part2(word: str) -> bool:
    # Ищем пару букв, которая повторяется позже и не пересекается с первой.
    has_repeated_pair = False
    for i in range(len(word) - 1):
        pair = word[i:i + 2]
        if pair in word[i + 2:]:
            has_repeated_pair = True
            break

    # Ищем букву, между одинаковыми экземплярами которой ровно одна буква.
    has_split_repeat = False
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            has_split_repeat = True
            break

    return has_repeated_pair and has_split_repeat


def solve(words: list[str]) -> tuple[int, int]:
    # Считаем, сколько строк подходят под правила каждой части.
    part1_count = sum(1 for word in words if nice_part1(word))
    part2_count = sum(1 for word in words if nice_part2(word))
    return part1_count, part2_count


if __name__ == '__main__':
    words = Path(__file__).with_name('input.txt').read_text().splitlines()
    part1_answer, part2_answer = solve(words)
    print(f'Part 1: {part1_answer}')
    print(f'Part 2: {part2_answer}')
