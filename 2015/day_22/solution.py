import heapq
from pathlib import Path


SPELLS = ((53, 'missile'), (73, 'drain'), (113, 'shield'),
          (173, 'poison'), (229, 'recharge'))


def least_mana(boss_hp: int, boss_damage: int, hard: bool = False) -> int:
    queue = [(0, 50, 500, boss_hp, 0, 0, 0)]
    best = {}
    while queue:
        spent, hp, mana, boss, shield, poison, recharge = heapq.heappop(queue)
        if spent >= best.get((hp, mana, boss, shield, poison, recharge), float('inf')):
            continue
        best[hp, mana, boss, shield, poison, recharge] = spent

        player_hp = hp - int(hard)
        if player_hp <= 0:
            continue
        if poison:
            boss -= 3
        if recharge:
            mana += 101
        shield = max(0, shield - 1)
        poison = max(0, poison - 1)
        recharge = max(0, recharge - 1)
        if boss <= 0:
            return spent

        for cost, spell in SPELLS:
            if mana < cost:
                continue
            if spell == 'shield' and shield or spell == 'poison' and poison or spell == 'recharge' and recharge:
                continue
            next_hp, next_mana, next_boss = player_hp, mana - cost, boss
            next_shield, next_poison, next_recharge = shield, poison, recharge
            if spell == 'missile':
                next_boss -= 4
            elif spell == 'drain':
                next_boss -= 2
                next_hp += 2
            elif spell == 'shield':
                next_shield = 6
            elif spell == 'poison':
                next_poison = 6
            else:
                next_recharge = 5
            next_spent = spent + cost
            if next_boss <= 0:
                return next_spent

            # Boss turn: effects apply before its attack.
            if next_poison:
                next_boss -= 3
            if next_recharge:
                next_mana += 101
            armor_active = next_shield > 0
            next_shield = max(0, next_shield - 1)
            next_poison = max(0, next_poison - 1)
            next_recharge = max(0, next_recharge - 1)
            if next_boss <= 0:
                return next_spent
            next_hp -= max(1, boss_damage - (7 if armor_active else 0))
            state = (next_hp, next_mana, next_boss, next_shield, next_poison, next_recharge)
            if next_hp > 0 and next_spent < best.get(state, float('inf')):
                heapq.heappush(queue, (next_spent, *state))
    raise ValueError('The boss cannot be defeated with the available spells')


def solve(lines: list[str]) -> tuple[int, int]:
    stats = {key: int(value) for line in lines if ': ' in line
             for key, value in [line.split(': ', 1)]}
    required = {'Hit Points', 'Damage'}
    if not required <= stats.keys():
        raise ValueError('Day 22 input must provide Hit Points and Damage')
    return least_mana(stats['Hit Points'], stats['Damage']), least_mana(stats['Hit Points'], stats['Damage'], hard=True)


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().splitlines()), sep='\n')
