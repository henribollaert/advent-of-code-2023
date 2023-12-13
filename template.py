import os
from timeit import default_timer as timer

DAY = "00"

def parse(lines: list[str]):
    pass

def part1(lines: list[str]) -> str:
    start = timer()

    end = timer()

    print(f'In {(end - start)*1000}ms.')

def part2(lines: list[str]) -> str:
    start = timer()

    end = timer()

    print(f'In {(end - start)*1000}ms.')

def main():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, f'input-{DAY}.txt'), 'r')
    lines = f.readlines()
    f.close()

    print("Score for part 1:", part1(lines))
    print("Score for part 2:", part2(lines))

if __name__ == "__main__":
    main()