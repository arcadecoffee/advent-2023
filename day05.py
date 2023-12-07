"""
Advent of Code 2023 Day 5
"""

import re
import sys

from typing import Iterable, Union

from aoc import get_daily_input

YEAR = 2023
DAY = 5

TEST = sys.argv[1] == "test" if len(sys.argv) > 1 else False

TEST_DATA = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

if TEST:
    def get_daily_input(*args, **kwargs):
        for line in TEST_DATA.strip().split("\n"):
            yield line.strip("\n")


def load_input(input: Iterable[str]) -> tuple[list[int], list[list[int]]]:
    results: dict[str, Union[list[int], list[list[int]]]] = {}

    seeds = list(map(int, next(input).split(" ")[1:]))
    maps: list[list[int]] = []

    for s in input:
        if s.endswith(" map:"):
            maps.append([])
        elif len(s):
            maps[-1].append(list(map(int, s.split(" "))))
    return seeds, maps


def find_smallest_location(seeds: list[int], maps: list[list[int]]) -> int:
    smallest: int = None
    for v in seeds:
        for m in maps:
            for n in m:
                if v >= n[1] and v < n[1] + n[2]:
                    v = n[0] + (v - n[1])
                    break
        if (not smallest) or v < smallest:
            smallest = v
            print(v)
    
    return smallest


def seed_generator(seed_values: list[int]) -> Iterable[int]:
    for i in range(0, len(seed_values), 2):
        for j in range(seed_values[i + 1]):
            yield seed_values[i] + j

def main() -> None:
    seeds, maps = load_input(get_daily_input(YEAR, DAY))

    part_1 = find_smallest_location(seeds, maps)
    print(f"Part 1: {part_1}")

    part_2 = find_smallest_location(seed_generator(seeds), maps)
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()