from pathlib import Path
import re

def parse(data: str) -> tuple[str, int, dict[str, dict[int, tuple[int, int, str]]]]:
    start_match = re.search(r"Begin in state (\w+)", data)
    steps_match = re.search(r"after (\d+) steps", data)
    if not start_match or not steps_match:
        raise ValueError("Input must include a starting state and diagnostic step count")
    transitions: dict[str, dict[int, tuple[int, int, str]]] = {}
    state_blocks = re.split(r"(?=In state \w+:)", data)
    for block in state_blocks:
        state_match = re.match(r"In state (\w+):", block.strip())
        if not state_match:
            continue
        state = state_match.group(1)
        branches = re.findall(
            r"If the current value is ([01]):\s*- Write the value ([01]).*?"
            r"- Move one slot to the (left|right).*?"
            r"- Continue with state (\w+)", block, re.S
        )
        transitions[state] = {
            int(value): (int(write), -1 if direction == "left" else 1, next_state)
            for value, write, direction, next_state in branches
        }
    return start_match.group(1), int(steps_match.group(1)), transitions

def checksum(data: str) -> int:
    state, steps, transitions = parse(data)
    tape: set[int] = set()
    cursor = 0
    for _ in range(steps):
        write, move, state = transitions[state][int(cursor in tape)]
        if write: tape.add(cursor)
        else: tape.discard(cursor)
        cursor += move
    return len(tape)

def part1(data: str) -> int: return checksum(data)
def part2(data: str) -> str: return "Merry Christmas!"

if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
