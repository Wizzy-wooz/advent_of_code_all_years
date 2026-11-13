from pathlib import Path

def valid_triangle(list):
    max_side = max(list)
    if max_side < (sum(list) - max_side):
        return 1
    return 0


if __name__ == '__main__':
    lines = Path(__file__).with_name('input.txt').read_text().splitlines()
    number = 0

    for line in lines:
        sides = [int(number) for number in line.split()]
        number = number + valid_triangle(sides)

    print(number)
