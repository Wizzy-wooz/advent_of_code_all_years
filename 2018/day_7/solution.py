from pathlib import Path
import re


def graph(data: str):
    deps: dict[str, set[str]] = {}
    for line in data.splitlines():
        if line.strip():
            a, b = re.findall(r"Step (\w) must be finished before step (\w) can begin", line)[0]
            deps.setdefault(a, set());
            deps.setdefault(b, set()).add(a)
    return deps


def order(data: str) -> str:
    deps = graph(data);
    done = ""
    while len(done) < len(deps):
        available = sorted(step for step, needs in deps.items() if step not in done and needs <= set(done))
        if not available: raise ValueError("Dependency graph contains a cycle")
        done += available[0]
    return done


def duration(data: str, workers: int = 5, base: int = 60) -> int:
    deps = graph(data);
    time = 0;
    done = set();
    working = {}
    while len(done) < len(deps):
        for step in sorted(deps):
            if len(working) >= workers: break
            if step not in done and step not in working and deps[step] <= done: working[step] = time + base + ord(
                step) - ord("A") + 1
        if not working: raise ValueError("Dependency graph contains a cycle")
        time = min(working.values())
        done.update(step for step, finish in working.items() if finish == time)
        working = {step: finish for step, finish in working.items() if finish > time}
    return time


def part1(data: str) -> str: return order(data)


def part2(data: str) -> int: return duration(data)


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
