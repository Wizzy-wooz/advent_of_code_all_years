from collections import Counter
from pathlib import Path
import re


ROOM_PATTERN = re.compile(r'([a-z-]+)-(\d+)\[([a-z]+)\]')


def parse_room(room: str) -> tuple[str, int, str]:
    match = ROOM_PATTERN.fullmatch(room.strip())
    if match is None:
        raise ValueError(f'Invalid room: {room!r}')
    name, sector_id, checksum = match.groups()
    return name, int(sector_id), checksum


def is_real_room(name: str, checksum: str) -> bool:
    letter_counts = Counter(name.replace('-', ''))
    expected = ''.join(
        letter for letter, _ in sorted(
            letter_counts.items(), key=lambda item: (-item[1], item[0])
        )[:5]
    )
    return expected == checksum


def part1(rooms: str) -> int:
    sector_id_sum = 0
    for room in rooms.splitlines():
        if not room.strip():
            continue
        name, sector_id, checksum = parse_room(room)
        if is_real_room(name, checksum):
            sector_id_sum += sector_id
    return sector_id_sum


def decrypt_name(name: str, sector_id: int) -> str:
    shift = sector_id % 26
    return ''.join(
        ' ' if char == '-' else chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        for char in name
    )


def part2(rooms: str, target: str = 'northpole object storage') -> int | None:
    for room in rooms.splitlines():
        if not room.strip():
            continue
        name, sector_id, checksum = parse_room(room)
        if is_real_room(name, checksum) and decrypt_name(name, sector_id) == target:
            return sector_id
    return None


if __name__ == '__main__':
    rooms = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(rooms)}')
    answer = part2(rooms)
    print(f'Part 2: {answer if answer is not None else "room not found"}')
