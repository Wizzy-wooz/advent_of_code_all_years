import re


def supports_tls(ip: str) -> bool:
    parts = re.split(r'[\[\]]', ip.strip())
    return any(any(s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1] for i in range(len(s) - 3)) for s in parts[::2]) and not any(any(s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1] for i in range(len(s) - 3)) for s in parts[1::2])


def supports_ssl(ip: str) -> bool:
    parts = re.split(r'[\[\]]', ip.strip())
    abas = {s[i:i + 3] for s in parts[::2] for i in range(len(s) - 2) if s[i] == s[i + 2] and s[i] != s[i + 1]}
    return any(f'{b}{a}{b}' in hyper for a, b, _ in abas for hyper in parts[1::2])


def part1(data: str) -> int: return sum(supports_tls(line) for line in data.splitlines())
def part2(data: str) -> int: return sum(supports_ssl(line) for line in data.splitlines())


if __name__ == '__main__':
    from pathlib import Path
    data = Path(__file__).with_name('input.txt').read_text()
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')
