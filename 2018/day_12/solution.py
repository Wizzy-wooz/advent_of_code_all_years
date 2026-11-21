from pathlib import Path


def parse(data: str):
    lines = data.splitlines();
    initial = lines[0].split(": ")[1]
    rules = {line[:5]: line[-1] == "#" for line in lines[1:] if "=>" in line}
    return {i for i, c in enumerate(initial) if c == "#"}, rules


def after(data: str, generations: int) -> int:
    plants, rules = parse(data);
    seen = {};
    generation = 0
    while generation < generations:
        if plants:
            low, high = min(plants), max(plants)
            shape = tuple(i - low for i in plants)
            if shape in seen:
                old_gen, old_low = seen[shape]
                cycle = generation - old_gen;
                shift = low - old_low
                repeats = (generations - generation) // cycle
                if repeats:
                    plants = {i + repeats * shift for i in plants};
                    generation += repeats * cycle;
                    continue
            else:
                seen[shape] = (generation, low)
            plants = {i for i in range(low - 2, high + 3) if
                      rules.get("".join("#" if j in plants else "." for j in range(i - 2, i + 3)), False)}
        generation += 1
    return sum(plants)


def part1(data: str) -> int: return after(data, 20)


def part2(data: str) -> int: return after(data, 50_000_000_000)


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
