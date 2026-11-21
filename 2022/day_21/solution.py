from fractions import Fraction
from pathlib import Path


def parse(d): return {a: b for a, b in (line.split(": ") for line in d.splitlines() if line.strip())}


def part1(d):
    g = parse(d)

    def val(n):
        if g[n].lstrip("-").isdigit(): return int(g[n])
        a, op, b = g[n].split();
        return {"+": lambda: val(a) + val(b), "-": lambda: val(a) - val(b), "*": lambda: val(a) * val(b),
                "/": lambda: val(a) // val(b)}[op]()

    return val("root")


def part2(d):
    g = parse(d)

    def form(n):
        if n == "humn": return Fraction(1), Fraction(0)
        if g[n].lstrip("-").isdigit(): return Fraction(0), Fraction(int(g[n]))
        a, op, b = g[n].split();
        x, y = form(a);
        u, v = form(b)
        if op == "+": return x + u, y + v
        if op == "-": return x - u, y - v
        if op == "*": return x * v + u * y, y * v
        if u: raise ValueError("Division by a variable expression is not supported")
        return x / v, y / v

    a, _, b = g["root"].split();
    x, y = form(a);
    u, v = form(b);
    return int((v - y) / (x - u))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
