import os
from timeit import default_timer as timer
from enum import Enum

DAY = "10"
TEST = True
TESTNR = ""

def tuple_sum(a, b):
    return tuple([x + y for x, y in zip(a, b)])


def parse(lines: list[str]):
    pass

#(row, column)
class Direction(Enum):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (1, 0)
    DOWN = (-1, 0)

# we also need to keep track of direction, are we coming from above or below

def next_step(previous: Direction, symbol) -> Direction:
    pass

def part1(lines: list[str]):
    scan = lines
    s = None
    Direction.
    for nr, line in enumerate(scan):
        if 'S' in line:
            s = (nr, line.index('S'))
            break
    starts = []
    for loc, symbols in zip(
        [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN], [ ['L', 'F', '-'], ['J', '7', '-'], ['F', '7', '|'], ['L', 'J', '|']]):
        if scan[s[0] + loc[0]][s[1] + loc[1]] in symbols:
            starts.append((s[0] + loc[0], s[1] + loc[1]))
    
    for start in starts:

    
    print(starts)
                
    


def part2(lines: list[str]):
    pass

def main():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, f'{"test" + TESTNR if TEST else "input"}-{DAY}.txt'), 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    for nr, function in enumerate([part1, part2]):
        start = timer()
        result = function(lines)
        end = timer()
        print(f"Score for part {nr + 1}: {result} in {(end - start)*1000}ms.")


if __name__ == "__main__":
    main()