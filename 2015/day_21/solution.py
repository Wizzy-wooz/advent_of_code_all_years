import itertools
from pathlib import Path


WEAPONS = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
ARMOR = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
RINGS = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]


def solve(lines: list[str]) -> tuple[int, int]:
    stats = {key: int(value) for line in lines if ': ' in line
             for key, value in [line.split(': ', 1)]}
    required = {'Hit Points', 'Damage', 'Armor'}
    if not required <= stats.keys():
        raise ValueError('Day 21 input must provide Hit Points, Damage, and Armor')
    boss_hp, boss_damage, boss_armor = stats['Hit Points'], stats['Damage'], stats['Armor']
    wins, losses = [], []
    for weapon in WEAPONS:
        for armor in ARMOR:
            for ring_count in range(3):
                for rings in itertools.combinations(RINGS, ring_count):
                    items = (weapon, armor, *rings)
                    cost = sum(item[0] for item in items)
                    damage = sum(item[1] for item in items)
                    defense = sum(item[2] for item in items)
                    player_turns = (boss_hp + max(1, damage - boss_armor) - 1) // max(1, damage - boss_armor)
                    boss_turns = (100 + max(1, boss_damage - defense) - 1) // max(1, boss_damage - defense)
                    (wins if player_turns <= boss_turns else losses).append(cost)
    return min(wins), max(losses)


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
