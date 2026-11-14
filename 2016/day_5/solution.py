from hashlib import md5


def passwords(door_id: str) -> tuple[str, str]:
    door_id = door_id.strip()
    sequential, positional = [], [''] * 8
    index = 0
    while len(sequential) < 8 or '' in positional:
        digest = md5(f'{door_id}{index}'.encode()).hexdigest()
        if digest.startswith('00000'):
            if len(sequential) < 8:
                sequential.append(digest[5])
            if digest[5] in '01234567' and not positional[int(digest[5])]:
                positional[int(digest[5])] = digest[6]
        index += 1
    return ''.join(sequential), ''.join(positional)


def part1(data: str) -> str: return passwords(data)[0]
def part2(data: str) -> str: return passwords(data)[1]


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    first, second = passwords(data)
    print(f'Part 1: {first}')
    print(f'Part 2: {second}')
