import re


def clock_signal(data: str, initial: int) -> bool:
    p=[line.split() for line in data.splitlines() if line.strip()]; r=dict.fromkeys('abcd',0); r['a']=initial; ip=0; expected=0; outputs=0; seen=set()
    def val(x): return int(x) if re.fullmatch(r'-?\d+',x) else r[x]
    while 0<=ip<len(p):
        state=(ip,tuple(r.values()),expected)
        if state in seen: return outputs>0
        seen.add(state)
        op,*args=p[ip]
        if op=='cpy' and args[1] in r: r[args[1]]=val(args[0])
        elif op=='inc' and args[0] in r: r[args[0]]+=1
        elif op=='dec' and args[0] in r: r[args[0]]-=1
        elif op=='jnz' and val(args[0])!=0: ip+=val(args[1]); continue
        elif op=='out':
            if val(args[0])!=expected: return False
            expected=1-expected; outputs+=1
        ip+=1
    return False


def part1(data: str) -> int:
    a=0
    while not clock_signal(data,a): a+=1
    return a


def part2(data: str) -> str: return 'Merry Christmas!'


if __name__ == '__main__':
    from pathlib import Path
    data=Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
