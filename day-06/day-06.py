import os
from timeit import default_timer as timer
from math import sqrt, ceil, floor, prod
from collections import namedtuple

DAY = "06"
TEST = False

Race = namedtuple("Race", "t d")

def parse(lines: list[str]) -> list[Race]:
    return [Race(x, y) for x, y in zip(*[[int(j) for j in lines[i].split(':')[1].split()] for i in range(2)])]

def times_for_race(race:Race) -> int:
    accel = int( (race.t - sqrt(race.t * race.t - 4 * race.d))/2 + 1 )
    return race.t - 2 * accel + 1


def part1(lines: list[str]):
    races = parse(lines)
    sol = 1

    for race in races:
        sol *= times_for_race(race)
    return sol

def part2(lines: list[str]):
    race = Race(*[int(lines[i].split(':')[1].replace(" ", "")) for i in range(2)])
    return times_for_race(race)

def main():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, f'{"test" if TEST else "input"}-{DAY}.txt'), 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    for nr, function in enumerate([part1, part2]):
        start = timer()
        result = function(lines)
        end = timer()
        print(f"Score for part {nr + 1}: {result} in {(end - start)*1000}ms.")


if __name__ == "__main__":
    main()