from pathlib import Path
import re

REQ = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def passports(d): return [dict(field.split(":") for field in p.split()) for p in d.strip().split("\n\n") if p.strip()]


def part1(d): return sum(REQ <= p.keys() for p in passports(d))


def valid(p):
    if not REQ <= p.keys(): return False
    try:
        return 1920 <= int(p["byr"]) <= 2002 and 2010 <= int(p["iyr"]) <= 2020 and 2020 <= int(p["eyr"]) <= 2030 and (
                    (p["hgt"].endswith("cm") and 150 <= int(p["hgt"][:-2]) <= 193) or (
                        p["hgt"].endswith("in") and 59 <= int(p["hgt"][:-2]) <= 76)) and bool(
            re.fullmatch(r"#[0-9a-f]{6}", p["hcl"])) and p["ecl"] in "amb blu brn gry grn hzl oth".split() and bool(
            re.fullmatch(r"\d{9}", p["pid"]))
    except ValueError:
        return False


def part2(d): return sum(valid(p) for p in passports(d))


if __name__ == "__main__":
    d = Path(__file__).with_name("input.txt").read_text();
    print("Part 1:", part1(d));
    print("Part 2:", part2(d))
