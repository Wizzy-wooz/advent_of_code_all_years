from pathlib import Path


def mix(d, key=1, rounds=1):
    original = list(enumerate(int(number) * key for number in d.split()))
    mixed = original.copy()
    for _ in range(rounds):
        for entry in original:
            index = mixed.index(entry)
            mixed.pop(index)
            destination = (index + entry[1]) % len(mixed)
            mixed.insert(destination, entry)
    zero = next(index for index, (_, value) in enumerate(mixed) if value == 0)
    return sum(mixed[(zero + offset) % len(mixed)][1] for offset in (1000, 2000, 3000))



def part1(d): return mix(d)


def part2(d): return mix(d, 811589153, 10)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
