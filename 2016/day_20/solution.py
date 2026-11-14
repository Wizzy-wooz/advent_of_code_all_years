
def allowed(data: str, maximum: int = 4294967295) -> tuple[int | None, int]:
    ranges = sorted(tuple(map(int, line.split('-'))) for line in data.splitlines() if line.strip())
    merged = []
    for lo, hi in ranges:
        if merged and lo <= merged[-1][1] + 1: merged[-1] = (merged[-1][0], max(hi, merged[-1][1]))
        else: merged.append((lo, hi))
    first = 0; count = 0
    for lo, hi in merged:
        if first < lo: count += lo - first
        first = max(first, hi + 1)
    if first <= maximum: count += maximum - first + 1
    lowest = 0
    for lo, hi in merged:
        if lowest < lo:
            break
        lowest = max(lowest, hi + 1)
    return (lowest if lowest is not None and lowest <= maximum else None), count


def part1(data: str) -> int | None: return allowed(data)[0]
def part2(data: str) -> int: return allowed(data)[1]


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
