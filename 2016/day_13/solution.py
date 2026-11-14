from collections import deque


def shortest(favorite: int, target=(31, 39)) -> int:
    q = deque([((1, 1), 0)]); seen = {(1, 1)}
    def open_cell(x, y): return x >= 0 and y >= 0 and (x*x + 3*x + 2*x*y + y + y*y + favorite).bit_count() % 2 == 0
    while q:
        (x, y), d = q.popleft()
        if (x, y) == target: return d
        for p in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if p not in seen and open_cell(*p): seen.add(p); q.append((p,d+1))
    raise ValueError('Target unreachable')


def reachable(favorite: int, limit=50) -> int:
    q = deque([((1,1),0)]); seen = {(1,1)}
    def open_cell(x,y): return x >= 0 and y >= 0 and (x*x+3*x+2*x*y+y+y*y+favorite).bit_count()%2 == 0
    while q:
        (x,y),d=q.popleft()
        if d == limit: continue
        for p in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if p not in seen and open_cell(*p): seen.add(p); q.append((p,d+1))
    return len(seen)


def part1(data: str) -> int: return shortest(int(data.strip()))
def part2(data: str) -> int: return reachable(int(data.strip()))


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
