from collections import deque
from itertools import permutations


def solve(data: str) -> tuple[int,int]:
    grid=data.splitlines(); points={int(c):(x,y) for y,row in enumerate(grid) for x,c in enumerate(row) if c.isdigit()}; dist={}
    for start,(sx,sy) in points.items():
        q=deque([((sx,sy),0)]); seen={(sx,sy)}
        while q:
            (x,y),d=q.popleft()
            for target,(tx,ty) in points.items():
                if (x,y)==(tx,ty): dist[start,target]=d
            for p in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0<=p[1]<len(grid) and 0<=p[0]<len(grid[p[1]]) and grid[p[1]][p[0]]!='#' and p not in seen: seen.add(p); q.append((p,d+1))
    others=sorted(set(points)-{0}); routes=[(sum(dist[a,b] for a,b in zip((0,)+perm,perm)), sum(dist[a,b] for a,b in zip((0,)+perm,perm+(0,)))) for perm in permutations(others)]
    return min(a for a,b in routes),min(b for a,b in routes)


def part1(data: str) -> int: return solve(data)[0]
def part2(data: str) -> int: return solve(data)[1]


if __name__ == '__main__':
    from pathlib import Path
    data=Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
