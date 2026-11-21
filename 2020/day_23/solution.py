from pathlib import Path


def play(data, total, moves):
    nums = list(map(int, data.strip()));
    maximum = max(total, max(nums));
    nxt = [0] * (maximum + 1)
    seq = nums + list(range(max(nums) + 1, maximum + 1));
    for a, b in zip(seq, seq[1:] + seq[:1]): nxt[a] = b
    cur = seq[0]
    for _ in range(moves):
        a = nxt[cur];
        b = nxt[a];
        c = nxt[b];
        nxt[cur] = nxt[c];
        dest = cur - 1 or maximum
        while dest in (a, b, c): dest = dest - 1 or maximum
        nxt[c] = nxt[dest];
        nxt[dest] = a;
        cur = nxt[cur]
    return nxt


def part1(d):
    n = play(d, 9, 100);
    out = [];
    x = n[1]
    while x != 1: out.append(str(x));x = n[x]
    return "".join(out)


def part2(d): n = play(d, 1_000_000, 10_000_000);return n[1] * n[n[1]]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
