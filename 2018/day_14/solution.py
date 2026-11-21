from pathlib import Path


def scores_after(count: int) -> str:
    scores = [3, 7];
    a, b = 0, 1
    while len(scores) < count + 10:
        total = scores[a] + scores[b]
        if total >= 10: scores.append(1)
        scores.append(total % 10)
        a = (a + scores[a] + 1) % len(scores);
        b = (b + scores[b] + 1) % len(scores)
    return "".join(map(str, scores[count:count + 10]))


def recipes_before(target: str) -> int:
    pattern = list(map(int, target));
    scores = [3, 7];
    a, b = 0, 1
    if scores[:len(pattern)] == pattern: return 0
    if scores[-len(pattern):] == pattern: return len(scores) - len(pattern)
    while True:
        total = scores[a] + scores[b]
        for digit in ([1, total % 10] if total >= 10 else [total]):
            scores.append(digit)
            if scores[-len(pattern):] == pattern: return len(scores) - len(pattern)
        a = (a + scores[a] + 1) % len(scores);
        b = (b + scores[b] + 1) % len(scores)


def part1(data: str) -> str: return scores_after(int(data.strip()))


def part2(data: str) -> int: return recipes_before(data.strip())


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
