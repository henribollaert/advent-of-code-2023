import os
from timeit import default_timer as timer

DAY = "00"
TEST = True
TESTNR = ""


def parse(lines: list[str]):
    pass

def part1(lines: list[str]):
    pass

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