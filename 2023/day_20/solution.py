from collections import deque
from math import lcm
from pathlib import Path


def parse(d):
    mods = {};
    outs = {}
    for line in d.splitlines():
        if line.strip(): a, b = line.split(" -> ");name = a.lstrip("%&");mods[name] = a[0];outs[name] = b.split(", ")
    return mods, outs


def simulate(d, presses=1000):
    mods, outs = parse(d);
    flip = {x: False for x, t in mods.items() if t == "%"};
    conj = {x: {} for x, t in mods.items() if t == "&"}
    for a, bs in outs.items():
        for b in bs:
            if b in conj: conj[b][a] = False
    low = high = 0;
    events = {};
    rx_parent = next((a for a, bs in outs.items() if "rx" in bs), None)
    for press in range(1, presses + 1):
        q = deque([("button", "broadcaster", False)])
        while q:
            src, dst, pulse = q.popleft();
            low += not pulse;
            high += pulse
            if dst == "rx" and not pulse: events["rx"] = press
            if dst not in mods: continue
            typ = mods[dst]
            if typ == "b":
                out = pulse
            elif typ == "%":
                if pulse: continue
                flip[dst] = not flip[dst];
                out = flip[dst]
            else:
                conj[dst][src] = pulse;
                out = not all(conj[dst].values())
            if dst == rx_parent and out: events[src] = events.get(src, []) + [press]
            q.extend((dst, b, out) for b in outs[dst])
        if press == presses: answer = low * high
    return answer, events


def part1(d): return simulate(d)[0]


def part2(d):
    _, e = simulate(d, 5_000_000)
    if "rx" in e: return e["rx"]
    cycles = [v[-1] - v[-2] for k, v in e.items() if isinstance(v, list) and len(v) >= 2]
    if not cycles: raise ValueError("Could not infer input cycles to rx")
    return lcm(*cycles)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
