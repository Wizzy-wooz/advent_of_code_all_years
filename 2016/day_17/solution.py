from collections import deque
from hashlib import md5


def paths(passcode: str) -> tuple[str, int]:
    q = deque([((0,0), '', passcode.strip())]); shortest = None; longest = 0
    while q:
        (x,y), path, key = q.popleft()
        if (x,y) == (3,3):
            if shortest is None: shortest = path
            longest = len(path); continue
        for ch, (dx,dy), door in zip('UDLR', ((0,-1),(0,1),(-1,0),(1,0)), md5(key.encode()).hexdigest()[:4]):
            nx,ny=x+dx,y+dy
            if door in 'bcdef' and 0 <= nx < 4 and 0 <= ny < 4: q.append(((nx,ny),path+ch,key+ch))
    return shortest or '', longest


def part1(data: str) -> str: return paths(data)[0]
def part2(data: str) -> int: return paths(data)[1]


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
