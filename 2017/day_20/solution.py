from collections import defaultdict
from itertools import combinations
from math import isqrt
from pathlib import Path
import re


Vector = tuple[int, int, int]
Particle = tuple[Vector, Vector, Vector]
VECTOR_PATTERN = re.compile(r"<\s*(-?\d+)\s*,\s*(-?\d+)\s*,\s*(-?\d+)\s*>")


def parse(data: str) -> list[Particle]:
    particles = []
    for line in data.splitlines():
        if not line.strip():
            continue
        vectors = [tuple(map(int, match)) for match in VECTOR_PATTERN.findall(line)]
        if len(vectors) != 3:
            raise ValueError(f"Invalid particle description: {line}")
        particles.append((vectors[0], vectors[1], vectors[2]))
    return particles  # type: ignore[return-value]


def asymptotic_distance(particle: Particle) -> tuple[int, int, int]:
    """Return doubled Manhattan-distance polynomial coefficients at large t."""
    position, velocity, acceleration = particle
    quadratic = linear = constant = 0
    for p, v, a in zip(position, velocity, acceleration):
        b = a + 2 * v
        c = 2 * p
        if a:
            sign = 1 if a > 0 else -1
            quadratic += abs(a)
            linear += sign * b
            constant += sign * c
        elif b:
            sign = 1 if b > 0 else -1
            linear += abs(b)
            constant += sign * c
        else:
            constant += abs(c)
    return quadratic, linear, constant


def part1(data: str) -> int:
    particles = parse(data)
    if not particles:
        raise ValueError("No particles in input")
    return min(range(len(particles)), key=lambda i: asymptotic_distance(particles[i]))


def axis_collision_times(p: int, v: int, a: int) -> set[int] | None:
    """Integer t >= 0 satisfying a*t^2 + (a+2v)*t + 2p == 0.

    None means the two particles have equal coordinates on this axis at every t.
    """
    quadratic, linear, constant = a, a + 2 * v, 2 * p
    if quadratic == 0:
        if linear == 0:
            return None if constant == 0 else set()
        numerator = -constant
        return {numerator // linear} if numerator % linear == 0 and numerator // linear >= 0 else set()

    discriminant = linear * linear - 4 * quadratic * constant
    if discriminant < 0:
        return set()
    root = isqrt(discriminant)
    if root * root != discriminant:
        return set()
    denominator = 2 * quadratic
    times = set()
    for numerator in (-linear - root, -linear + root):
        if numerator % denominator == 0:
            time = numerator // denominator
            if time >= 0:
                times.add(time)
    return times


def collision_times(first: Particle, second: Particle) -> set[int]:
    common: set[int] | None = None
    for axis in range(3):
        p = first[0][axis] - second[0][axis]
        v = first[1][axis] - second[1][axis]
        a = first[2][axis] - second[2][axis]
        times = axis_collision_times(p, v, a)
        if times is not None:
            common = times if common is None else common & times
            if not common:
                return set()
    # Identical trajectories coincide from the start.
    return common if common is not None else {0}


def position_at(particle: Particle, time: int) -> Vector:
    p, v, a = particle
    return tuple(p[i] + v[i] * time + a[i] * time * (time + 1) // 2 for i in range(3))  # type: ignore[return-value]


def part2(data: str) -> int:
    particles = parse(data)
    events: set[int] = set()
    for first, second in combinations(particles, 2):
        events.update(collision_times(first, second))

    alive = set(range(len(particles)))
    for time in sorted(events):
        at_position: dict[Vector, list[int]] = defaultdict(list)
        for index in alive:
            at_position[position_at(particles[index], time)].append(index)
        for indices in at_position.values():
            if len(indices) > 1:
                alive.difference_update(indices)
    return len(alive)


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
