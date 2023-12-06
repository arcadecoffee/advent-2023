"""
Advent of Code 2023 Day 3
"""

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


def main() -> None:
    data = list([f".{d}." for d in get_daily_input(YEAR, DAY)])
    data = ["." * len(data[0])] + data + ["." * len(data[0])]

    numbers: list[dict[str, int]] = []
    for r in range(1, len(data) - 1):
        for m in re.finditer(r"\d+", data[r]):
            adjacents = data[r - 1][m.start() - 1:m.end() + 1] + data[r][m.start() - 1] + data[r][m.end()] + data[r + 1][m.start() - 1:m.end() + 1]
            valid = any([n != "." for n in adjacents])
            numbers.append(
                {
                    "value": int(m.group()),
                    "row": r,
                    "start": m.start(),
                    "end": m.end(),
                    "adjacents": adjacents,
                    "valid": valid
                }
            )

    part_1 = sum([n["value"] for n in numbers if n["valid"]])
    print(f"Part 1: {part_1}")

    part_2 = -1
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()