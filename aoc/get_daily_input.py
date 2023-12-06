"""
Fetch, cache, and access your input data from Advent of Code
https://adventofcode.com
"""
import os
from typing import Iterable
from urllib.request import Request, urlopen

_URL_TEMPLATE = "https://adventofcode.com/{year}/day/{day}/input"

_DEFAULT_SESSION = os.environ.get("AOC_SESSION")
_DEFAULT_USERAGENT = os.environ.get("AOC_USERAGENT")

_CACHE_DIRECTORY = ".aoccache"


def _cache_filename(year: int, day: int):
    return f"{_CACHE_DIRECTORY}/{year}/{day}.txt"


def download_daily_input(year: int, day: int, session_id: str, useragent: str) -> None:
    """
    Yield lines from the day's input set
    """
    print(_URL_TEMPLATE.format(year=year, day=day))
    with urlopen(Request(
            url=_URL_TEMPLATE.format(year=year, day=day),
            headers={"Cookie": f"session={session_id}", "User-Agent": useragent}
    )) as response:
        if response.status == 200:
            os.makedirs(f"{_CACHE_DIRECTORY}/{year}", exist_ok=True)
            with open(_cache_filename(year, day), mode="wt") as outfile:
                for line in response:
                    outfile.write(line.decode())


def get_daily_input(
        year: int,
        day: int,
        session_id: str = _DEFAULT_SESSION,
        useragent: str = _DEFAULT_USERAGENT,
        force_download: bool = False
) -> Iterable[str]:
    if force_download or not os.path.exists(_cache_filename(year, day)):
        download_daily_input(year, day, session_id, useragent)
    with open(_cache_filename(year, day), mode="rt") as infile:
        for line in infile:
            yield line.strip("\n")
