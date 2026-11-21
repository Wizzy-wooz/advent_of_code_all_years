from collections import deque
from math import lcm
from pathlib import Path


def parse(d):
    mods = {};
    outs = {}
    for line in d.splitlines():
        if line.strip(): a, b = line.split(" -> ");name = a.lstrip("%&");mods[name] = a[0];outs[name] = b.split(", ")
    return mods, outs


def simulate(d, presses=1000, find_rx=False):
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
            if find_rx and dst == "rx" and not pulse:
                return press
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
            if find_rx and dst == rx_parent and pulse:
                hits = events.setdefault(src, [])
                if not hits or hits[-1] != press:
                    hits.append(press)
                if all(len(events.get(source, [])) >= 3 for source in conj[rx_parent]):
                    periods = []
                    for values in events.values():
                        period = values[1] - values[0]
                        if values[0] != period or values[2] != 3 * period:
                            break
                        periods.append(period)
                    else:
                        return lcm(*periods)
            q.extend((dst, b, out) for b in outs[dst])
        if press == presses: answer = low * high
    if find_rx:
        raise ValueError("Unable to determine the first low pulse at rx")
    return answer


def part1(d): return simulate(d)


def part2(d):
    return simulate(d, 5_000_000, find_rx=True)


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
