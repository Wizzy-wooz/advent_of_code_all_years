from pathlib import Path


def layers(data, w=25, h=6):
    digits = list(map(int, data.strip()));
    size = w * h
    return [digits[i:i + size] for i in range(0, len(digits), size)]


def part1(data):
    ls = layers(data);
    layer = min(ls, key=lambda x: x.count(0));
    return layer.count(1) * layer.count(2)


def part2(data, w=25, h=6):
    ls = layers(data, w, h);
    pixels = [next(layer[i] for layer in ls if layer[i] != 2) for i in range(w * h)]
    return "\n".join("".join("#" if pixels[y * w + x] else " " for x in range(w)).rstrip() for y in range(h))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:\n" + part2(d))
