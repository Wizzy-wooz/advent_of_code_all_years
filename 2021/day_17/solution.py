from pathlib import Path
import re


def solve(d):
    x1, x2, y1, y2 = map(int, re.findall(r"-?\d+", d));
    best = 0;
    count = 0
    for vx0 in range(min(0, x1), max(0, x2) + 1):
        for vy0 in range(y1, abs(y1) * 2 + 2):
            x = y = 0;
            vx = vx0;
            vy = vy0;
            peak = 0
            while x <= x2 and y >= y1:
                x += vx;
                y += vy;
                peak = max(peak, y);
                vx -= (vx > 0) - (vx < 0);
                vy -= 1
                if x1 <= x <= x2 and y1 <= y <= y2: best = max(best, peak);count += 1;break
    return best, count


def part1(d): return solve(d)[0]


def part2(d): return solve(d)[1]


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
