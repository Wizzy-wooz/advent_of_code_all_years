from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]));
from intcode import Computer


def play(data):
    c = Computer(list(map(int, data.strip().split(","))));
    transcript = ""
    while not c.halted:
        out = c.run();
        text = "".join(map(chr, (x for x in out if 0 <= x < 128)));
        transcript += text
        print(text, end="")
        if not c.halted:
            try:
                command = input()
            except EOFError:
                break
            c.inputs.extend(map(ord, command + "\n"))
    return transcript


def part1(data): return play(data)


def part2(data): return "Merry Christmas!"


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
