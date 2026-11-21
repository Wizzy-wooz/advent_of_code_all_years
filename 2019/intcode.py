from collections import defaultdict, deque


class Computer:
    def __init__(self, program, inputs=()):
        self.mem = defaultdict(int, enumerate(program));
        self.ip = 0;
        self.base = 0;
        self.inputs = deque(inputs);
        self.halted = False

    def run(self):
        out = []
        while not self.halted:
            ins = self.mem[self.ip];
            op = ins % 100;
            modes = ins // 100

            def mode(i):
                return (modes // (10 ** (i - 1))) % 10

            def read(i):
                p = self.mem[self.ip + i];
                m = mode(i)
                return self.mem[p] if m == 0 else self.mem[self.base + p] if m == 2 else p

            def addr(i):
                p = self.mem[self.ip + i];
                return p + self.base if mode(i) == 2 else p

            if op == 99: self.halted = True;break
            if op in (1, 2, 7, 8):
                a, b = read(1), read(2);
                self.mem[addr(3)] = {1: a + b, 2: a * b, 7: int(a < b), 8: int(a == b)}[op];
                self.ip += 4
            elif op == 3:
                if not self.inputs: break
                self.mem[addr(1)] = self.inputs.popleft();
                self.ip += 2
            elif op == 4:
                out.append(read(1));self.ip += 2
            elif op in (5, 6):
                a, b = read(1), read(2);
                self.ip = b if (a != 0 if op == 5 else a == 0) else self.ip + 3
            elif op == 9:
                self.base += read(1);self.ip += 2
            else:
                raise ValueError(f"Unknown opcode {op} at {self.ip}")
        return out
