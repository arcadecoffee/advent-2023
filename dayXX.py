"""
Advent of Code 2023 Day 0
"""

import sys

from aoc import get_daily_input

YEAR = 2023
DAY = 0

TEST = sys.argv[1] == "test" if len(sys.argv) > 1 else False

TEST_DATA = """
"""

if TEST:
    def get_daily_input(*args, **kwargs):
        for line in TEST_DATA.strip().split("\n"):
            yield line.strip("\n")


def main() -> None:
    data = list(get_daily_input(YEAR, DAY))
    print(data)


if __name__ == "__main__":
    main()