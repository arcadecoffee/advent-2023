"""
Advent of Code 2023 Day 4
"""

import re
import sys

from aoc import get_daily_input

YEAR = 2023
DAY = 4

TEST = sys.argv[1] == "test" if len(sys.argv) > 1 else False

TEST_DATA = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

if TEST:
    def get_daily_input(*args, **kwargs):
        for line in TEST_DATA.strip().split("\n"):
            yield line.strip("\n")


def calculate_score(data: list[str]) -> int:
    score = 0
    for card in data:
        winners, mine = re.match(r"^Card +\d+: ([ \d]+) \| ([ \d]+)$", card).groups()
        winners = [int(r) for r in re.findall(r".\d+", winners)]
        mine = [int(r) for r in re.findall(r".\d+", mine)]
        matches = [m for m in mine if m in winners]
        if matches:
            score += 2**(len(matches) - 1)
    return score


def count_cards(data: list[str]) -> int:
    cards = [{"count": 1, "card": c} for c in data]
    for c in range(len(cards)):
        winners, mine = re.match(r"^Card +\d+: ([ \d]+) \| ([ \d]+)$", cards[c]["card"]).groups()
        winners = [int(r) for r in re.findall(r".\d+", winners)]
        mine = [int(r) for r in re.findall(r".\d+", mine)]
        matches = [m for m in mine if m in winners]
        for i in range(len(matches)):
            cards[c + i + 1]["count"] += cards[c]["count"]
    return sum([c["count"] for c in cards])


def main() -> None:
    data = list(get_daily_input(YEAR, DAY))

    part_1 = calculate_score(data)
    print(f"Part 1: {part_1}")

    part_2 = count_cards(data)
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()