from pathlib import Path
import re


def parse(data: str):
    armies = [];
    current = None
    for line in data.splitlines():
        if line.endswith(":"):
            current = line[:-1].lstrip("= ")
            armies.append((current, []))
        elif line.strip():
            m = re.fullmatch(
                r"(\d+) units each with (\d+) hit points(?: \((.*?)\))? with an attack that does (\d+) (\w+) damage at initiative (\d+)",
                line.strip())
            n, hp, special, damage, kind, initiative = m.groups();
            weak = set();
            immune = set()
            if special:
                for part in special.split("; "):
                    dest = weak if part.startswith("weak") else immune
                    dest.update(part.split(" to ")[1].split(", "))
            armies[-1][1].append([int(n), int(hp), int(damage), kind, int(initiative), weak, immune])
    return armies


def fight(data: str, boost: int = 0):
    armies = parse(data)
    for group in armies[0][1]: group[2] += boost
    while all(groups for _, groups in armies):
        if len(armies[0][1]) == 0 or len(armies[1][1]) == 0: break
        order = []
        for ai, (_, groups) in enumerate(armies):
            for gi, group in enumerate(groups): order.append((group[0] * group[2], group[4], ai, gi))
        order.sort(reverse=True);
        chosen = set();
        targets = {}
        for power, initiative, ai, gi in order:
            attacker = armies[ai][1][gi]
            choices = []
            for bi, (_, groups) in enumerate(armies):
                if bi == ai: continue
                for bj, target in enumerate(groups):
                    if (bi, bj) in chosen: continue
                    multiplier = 0 if attacker[3] in target[6] else 2 if attacker[3] in target[5] else 1
                    if multiplier:
                        damage = attacker[0] * attacker[2] * multiplier
                        effective_power = target[0] * target[2]
                        choices.append((damage, effective_power, target[4], bi, bj))
            if choices:
                _, _, _, bi, bj = max(choices)
                targets[(ai, gi)] = (bi, bj);
                chosen.add((bi, bj))
        killed = 0
        for power, initiative, ai, gi in sorted(order, reverse=True, key=lambda item: item[1]):
            if gi >= len(armies[ai][1]): continue
            if armies[ai][1][gi][0] <= 0: continue
            target_ref = targets.get((ai, gi))
            if not target_ref: continue
            bi, bj = target_ref;
            attacker = armies[ai][1][gi];
            defenders = armies[bi][1]
            if bj >= len(defenders): continue
            target = defenders[bj];
            mult = 0 if attacker[3] in target[6] else 2 if attacker[3] in target[5] else 1
            dead = min(target[0], attacker[0] * attacker[2] * mult // target[1]);
            target[0] -= dead;
            killed += dead
        for _, groups in armies: groups[:] = [g for g in groups if g[0] > 0]
        if killed == 0: return None, None
    winner = armies[0] if armies[0][1] else armies[1]
    return winner[0], sum(g[0] for g in winner[1])


def part1(data: str) -> int:
    result = fight(data)
    if result[1] is None: raise ValueError("Battle stalemated")
    return result[1]


def part2(data: str) -> int:
    boost = 0
    while True:
        winner, units = fight(data, boost)
        if winner == "Immune System": return units
        boost += 1


if __name__ == "__main__":
    data = Path(__file__).with_name("input.txt").read_text()
    print("Part 1:", part1(data));
    print("Part 2:", part2(data))
