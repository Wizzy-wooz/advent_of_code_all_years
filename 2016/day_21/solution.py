import re


def scramble(data: str, password: str) -> str:
    chars = list(password)
    for line in data.splitlines():
        if m := re.fullmatch(r'swap position (\d+) with position (\d+)', line):
            x,y=map(int,m.groups()); chars[x],chars[y]=chars[y],chars[x]
        elif m := re.fullmatch(r'swap letter (.) with letter (.)', line):
            x,y=m.groups(); chars=[y if c==x else x if c==y else c for c in chars]
        elif m := re.fullmatch(r'rotate (left|right) (\d+) steps?', line):
            n=int(m[2])%len(chars); n=n if m[1]=='right' else -n; chars=chars[-n:]+chars[:-n] if n else chars
        elif m := re.fullmatch(r'rotate based on position of letter (.)', line):
            i=chars.index(m[1]); n=1+i+(i>=4); n%=len(chars); chars=chars[-n:]+chars[:-n] if n else chars
        elif m := re.fullmatch(r'reverse positions (\d+) through (\d+)', line):
            x,y=map(int,m.groups()); chars[x:y+1]=reversed(chars[x:y+1])
        elif m := re.fullmatch(r'move position (\d+) to position (\d+)', line):
            x,y=map(int,m.groups()); chars.insert(y,chars.pop(x))
    return ''.join(chars)


def unscramble(data: str, password: str) -> str:
    # The rotate-by-letter operation is not one-to-one by direct inversion for every length;
    # test each possible predecessor and retain the one that replays to the target.
    current = {password}
    lines = data.splitlines()
    for line in reversed(lines):
        candidates = set()
        for word in current:
            if line.startswith('rotate based on position'):
                for n in range(len(word)):
                    prev = word[n:] + word[:n]
                    if scramble(line, prev) == word: candidates.add(prev)
            else:
                # Invert a single instruction by reversing its operation.
                m = re.fullmatch(r'swap position (\d+) with position (\d+)', line)
                if m:
                    a=list(word); x,y=map(int,m.groups()); a[x],a[y]=a[y],a[x]; candidates.add(''.join(a)); continue
                m = re.fullmatch(r'swap letter (.) with letter (.)', line)
                if m: candidates.add(scramble(line, word)); continue
                m = re.fullmatch(r'rotate (left|right) (\d+) steps?', line)
                if m:
                    n=int(m[2])%len(word); n=-n if m[1]=='right' else n; candidates.add(word[-n:]+word[:-n] if n else word); continue
                m = re.fullmatch(r'reverse positions (\d+) through (\d+)', line)
                if m:
                    a=list(word); x,y=map(int,m.groups()); a[x:y+1]=reversed(a[x:y+1]); candidates.add(''.join(a)); continue
                m = re.fullmatch(r'move position (\d+) to position (\d+)', line)
                if m:
                    a=list(word); x,y=map(int,m.groups()); a.insert(x,a.pop(y)); candidates.add(''.join(a))
        current = candidates
    if len(current) != 1: raise ValueError(f'Expected one unscrambled password, got {current}')
    return current.pop()


def part1(data: str) -> str: return scramble(data, 'abcdefgh')
def part2(data: str) -> str: return unscramble(data, 'fbgdceah')


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
