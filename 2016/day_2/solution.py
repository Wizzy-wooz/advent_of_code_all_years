from pathlib import Path


def part1(instructions: list[str]) -> str:
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
    ]

    # Кнопка 5 находится в строке 1, столбце 1.
    row = 1
    column = 1
    code = ''

    for line in instructions:
        for move in line:
            new_row = row
            new_column = column

            if move == 'U':
                new_row -= 1
            elif move == 'D':
                new_row += 1
            elif move == 'L':
                new_column -= 1
            elif move == 'R':
                new_column += 1

            # На обычной клавиатуре все клетки — кнопки.
            if 0 <= new_row < 3 and 0 <= new_column < 3:
                row = new_row
                column = new_column

        code += keypad[row][column]

    return code


def part2(instructions: list[str]) -> str:
    keypad = [
        [' ', ' ', '1', ' ', ' '],
        [' ', '2', '3', '4', ' '],
        ['5', '6', '7', '8', '9'],
        [' ', 'A', 'B', 'C', ' '],
        [' ', ' ', 'D', ' ', ' '],
    ]

    # Кнопка 5 находится в строке 2, столбце 0.
    row = 2
    column = 0
    code = ''

    for line in instructions:
        for move in line:
            new_row = row
            new_column = column

            if move == 'U':
                new_row -= 1
            elif move == 'D':
                new_row += 1
            elif move == 'L':
                new_column -= 1
            elif move == 'R':
                new_column += 1

            # Переходим только на существующую кнопку, не на пустую клетку.
            if (0 <= new_row < len(keypad)
                    and 0 <= new_column < len(keypad[new_row])
                    and keypad[new_row][new_column] != ' '):
                row = new_row
                column = new_column

        code += keypad[row][column]

    return code


if __name__ == '__main__':
    instructions = Path(__file__).with_name('input.txt').read_text().splitlines()
    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2(instructions)}')
