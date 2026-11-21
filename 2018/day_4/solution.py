from collections import defaultdict
from datetime import datetime
from pathlib import Path
import re


def guards(data: str):
    events = sorted(line.strip() for line in data.splitlines() if line.strip())
    asleep: dict[int, list[int]] = defaultdict(lambda: [0] * 60)
    guard = fell_asleep = None
    for line in events:
        stamp = datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
        action = line[19:]
        if "begins shift" in action:
            guard = int(re.search(r"#(\d+)", action).group(1))
        elif action == "falls asleep":
            fell_asleep = stamp.minute
        elif action == "wakes up":
            for minute in range(fell_asleep, stamp.minute): asleep[guard][minute] += 1
    return asleep


def results(data: str) -> tuple[int, int]:
    asleep = guards(data)
    sleepy = max(asleep, key=lambda guard: sum(asleep[guard]))
    minute = max(range(60), key=lambda m: asleep[sleepy][m])
    guard2 = max(asleep, key=lambda guard: max(asleep[guard]))
    minute2 = max(range(60), key=lambda m: asleep[guard2][m])
    return sleepy * minute, guard2 * minute2


def part1(data: str) -> int: return results(data)[0]


def part2(data: str) -> int: return results(data)[1]


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
