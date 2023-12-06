"""
Advent of Code 2023 Day 1
"""

import re
import sys

from typing import Iterable

from aoc import get_daily_input

YEAR = 2023
DAY = 1

TEST = sys.argv[1] == "test" if len(sys.argv) > 1 else True

TEST_DATA = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
two1nine
eightwo0three
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

if TEST:
    def get_daily_input(*args, **kwargs):
        for line in TEST_DATA.strip().split("\n"):
            yield line.strip("\n")


def translate_digit(input: str) -> str:
    words_to_numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    return input if input.isdigit() else words_to_numbers[input]


def get_digits_and_words(input: str) -> int:
    first = translate_digit(re.match(r".*?(\d|one|two|three|four|five|six|seven|eight|nine)", input)[1])
    last = translate_digit(re.match(r".*(\d|one|two|three|four|five|six|seven|eight|nine).*?", input)[1])
    return int(first + last)


def get_digits(input: str) -> int:
    first = re.match(r".*?(\d)", input)[1]
    last = re.match(r".*(\d).*?", input)[1]
    return int(first + last)


def main() -> None:
    part_1 = sum([get_digits(d) for d in get_daily_input(YEAR, DAY)])
    print(f"Part 1: {part_1}")

    part_2 = sum([get_digits_and_words(d) for d in get_daily_input(YEAR, DAY)])
    print(f"Part 2: {part_2}")

if __name__ == "__main__":
    main()