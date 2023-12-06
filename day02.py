"""
Advent of Code 2023 Day 2
"""

import math
import re
import sys

from dataclasses import dataclass

from aoc import get_daily_input

YEAR = 2023
DAY = 2

TEST = sys.argv[1] == "test" if len(sys.argv) > 1 else False

TEST_DATA = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

if TEST:
    def get_daily_input(*args, **kwargs):
        for line in TEST_DATA.strip().split("\n"):
            yield line.strip("\n")


@dataclass
class Game:
    id: int
    rounds: dict[str, int]

    @classmethod
    def parse_game(cls, input: str) -> "Game":
        id, rounds_str = re.match(r"Game (\d+): (.*)", input).groups()
        rounds_list: list[dict[str, int]] = []

        for r in rounds_str.split("; "):
            round_dict = {k: int(v) for (v, k) in [c.split(" ") for c in r.split(", ")]}
            rounds_list.append(round_dict)

        return cls(id=int(id), rounds=rounds_list)


def sum_valid_games(games: list[Game], limits: dict[str, int]) -> int:
    return sum([g.id for g in games if all([max([r.get(c, 0) for r in g.rounds]) <= limits[c] for c in limits])])


def sum_game_powers(games: list[Game], limits: dict[str, int]) -> int:
    return sum([math.prod([max(r.get(c, 0) for r in g.rounds) for c in limits]) for g in games])


def main() -> None:
    limits = {"red": 12, "green": 13, "blue": 14}
    games = [Game.parse_game(d) for d in get_daily_input(YEAR, DAY)]

    part_1 = sum_valid_games(games, limits)
    print(f"Part 1: {part_1}")

    part_2 = sum_game_powers(games, limits)
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()