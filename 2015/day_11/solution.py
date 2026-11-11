from pathlib import Path


def valid(password: str) -> bool:
    if any(c in password for c in 'iol'):
        return False
    straight = any(ord(password[i]) + 1 == ord(password[i + 1])
                   and ord(password[i + 1]) + 1 == ord(password[i + 2])
                   for i in range(len(password) - 2))
    pairs = {password[i] for i in range(len(password) - 1)
             if password[i] == password[i + 1]}
    return straight and len(pairs) >= 2


def next_password(password: str) -> str:
    chars = list(password)
    while True:
        i = len(chars) - 1
        while i >= 0 and chars[i] == 'z':
            chars[i] = 'a'
            i -= 1
        if i < 0:
            chars.insert(0, 'a')
        else:
            chars[i] = chr(ord(chars[i]) + 1)
        for j, char in enumerate(chars):
            if char in 'iol':
                chars[j] = chr(ord(char) + 1)
                chars[j + 1:] = ['a'] * (len(chars) - j - 1)
                break
        candidate = ''.join(chars)
        if valid(candidate):
            return candidate


def solve(password: str) -> tuple[str, str]:
    first = next_password(password)
    return first, next_password(first)


if __name__ == '__main__':
    print(*solve(Path(__file__).with_name('input.txt').read_text().strip()), sep='\n')
