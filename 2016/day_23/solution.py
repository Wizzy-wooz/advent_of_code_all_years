import re


def execute(data: str, a: int) -> int:
    p=[line.split() for line in data.splitlines() if line.strip()]; r=dict.fromkeys('abcd',0); r['a']=a; ip=0
    def val(x): return int(x) if re.fullmatch(r'-?\d+',x) else r[x]
    while 0<=ip<len(p):
        # Collapse the nested add/decrement loop used to multiply two registers.
        if ip + 5 < len(p):
            block = p[ip:ip + 6]
            if (block[0][0] == 'cpy' and block[1][0] == 'inc' and block[2] == ['dec', block[0][2]]
                    and block[3] == ['jnz', block[0][2], '-2'] and block[4][0] == 'dec'
                    and block[5] == ['jnz', block[4][1], '-5']):
                source, counter, accumulator, outer = block[0][1], block[0][2], block[1][1], block[4][1]
                if len({counter, accumulator, outer}) == 3 and counter in r and accumulator in r and outer in r:
                    r[accumulator] += val(source) * r[outer]
                    r[counter] = r[outer] = 0
                    ip += 6
                    continue
        op,*args=p[ip]
        if op=='cpy' and args[1] in r: r[args[1]]=val(args[0])
        elif op=='inc' and args[0] in r: r[args[0]]+=1
        elif op=='dec' and args[0] in r: r[args[0]]-=1
        elif op=='jnz' and val(args[0])!=0: ip+=val(args[1]); continue
        elif op=='tgl':
            j=ip+val(args[0])
            if 0<=j<len(p):
                inst=p[j]; inst[0]=('dec' if inst[0]=='inc' else 'inc') if len(inst)==2 else ('cpy' if inst[0]=='jnz' else 'jnz')
        ip+=1
    return r['a']


def part1(data: str) -> int: return execute(data,7)
def part2(data: str) -> int: return execute(data,12)


if __name__ == '__main__':
    from pathlib import Path
    data=Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
