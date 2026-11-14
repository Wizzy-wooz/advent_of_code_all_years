import re
from collections import deque


def nodes(data: str):
    result={}
    for line in data.splitlines():
        m=re.search(r'x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T',line)
        if m:
            x,y,size,used=map(int,m.groups()); result[x,y]=(size,used)
    return result


def part1(data: str) -> int:
    values=list(nodes(data).values())
    return sum(a[1] > 0 and a[1] <= b[0] - b[1] for i, a in enumerate(values) for j, b in enumerate(values) if i != j)


def part2(data: str) -> int:
    ns=nodes(data); empty=next(p for p,v in ns.items() if v[1]==0); goal=(max(x for x,y in ns),0)
    # Treat large used nodes as fixed walls; the puzzle grid's movable data is the empty slot.
    wall={p for p,(size,used) in ns.items() if used > ns[empty][0]}
    q=deque([(empty,goal,0)]); seen={(empty,goal)}
    while q:
        hole,g,d=q.popleft()
        if g==(0,0): return d
        for p in ((hole[0]+1,hole[1]),(hole[0]-1,hole[1]),(hole[0],hole[1]+1),(hole[0],hole[1]-1)):
            if p not in ns or p in wall: continue
            ng=hole if p==g else g; state=(p,ng)
            if state not in seen: seen.add(state); q.append((p,ng,d+1))
    raise ValueError('Goal data cannot reach origin')


if __name__ == '__main__':
    from pathlib import Path
    data=Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
