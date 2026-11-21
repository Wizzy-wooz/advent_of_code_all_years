from pathlib import Path


def mix(d, key=1, rounds=1):
    a = [int(x) * key for x in d.split()];
    order = list(enumerate(a));
    n = len(a)
    for _ in range(rounds):
        for item in order:
            i = a.index(item[1]) if False else next(
                i for i, x in enumerate(a) if x == item[1] and order[i][0] == item[0])
            val = a.pop(i);
            pair = order.pop(i);
            j = (i + val) % (n - 1);
            a.insert(j, val);
            order.insert(j, pair)
    zero = a.index(0);
    return sum(a[(zero + k) % n] for k in (1000, 2000, 3000))


def part1(d): return mix(d)


def part2(d): return mix(d, 811589153, 10)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
