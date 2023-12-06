"""
Advent of Code 2023 Day 3
"""

import math
import re
import sys

from typing import Iterable

from aoc import get_daily_input

YEAR = 2023
DAY = 3

TEST = sys.argv[1] == "test" if len(sys.argv) > 1 else False

TEST_DATA = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

if TEST:
    def get_daily_input(*args, **kwargs):
        for line in TEST_DATA.strip().split("\n"):
            yield line.strip("\n")

def sum_real_part_numbers(data: list[str]) -> int:
    total = 0
    for r in range(1, len(data) - 1):
        for m in re.finditer(r"\d+", data[r]):
            adjacents = data[r - 1][m.start() - 1:m.end() + 1] + data[r][m.start() - 1] + data[r][m.end()] + data[r + 1][m.start() - 1:m.end() + 1]
            if any([n != "." for n in adjacents]):
                total += int(m.group()) 
    return total


def sum_gear_ratios(data: list[str]) -> int:
    gears: dict[tuple[str, str], list[int]] = {}
    for r in range(1, len(data) - 1):
        for m in re.finditer(r"\d+", data[r]):
            value = int(m.group())
            for c in range(m.start() - 1, m.end() + 1):
                if data[r - 1][c] == "*":
                    gears[(r - 1, c)] = gears.get((r - 1, c), []) + [value]
                if data[r + 1][c] == "*":
                    gears[(r + 1, c)] = gears.get((r + 1, c), []) + [value]
            if data[r][m.start() - 1] == "*":
                gears[(r, m.start() - 1)] = gears.get((r, m.start() - 1), []) + [value]
            if data[r][m.end()] == "*":
                gears[(r, m.end())] = gears.get((r, m.end()), []) + [value]
    return sum([math.prod(v) for v in gears.values() if len(v) == 2])


def main() -> None:
    data = list([f".{d}." for d in get_daily_input(YEAR, DAY)])
    data = ["." * len(data[0])] + data + ["." * len(data[0])]   # put a border around the schematic

    part_1 = sum_real_part_numbers(data)
    print(f"Part 1: {part_1}")

    part_2 = sum_gear_ratios(data)
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()