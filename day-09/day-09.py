import os
from timeit import default_timer as timer

DAY = "09"
TEST = False
TESTNR = ""


def parse(lines: list[str]):
    return [[int(i) for i in line.split()] for line in lines]

def differences(line):
    diffs = []
    for i, val in enumerate(line[1:]):
        diffs.append(val - line[i])
    return diffs

def part1(lines: list[str]):
    lines = parse(lines)
    total = 0
    for line in lines:
        while(not all(v == 0 for v in line)):
            total += line[-1]
            line = differences(line)
    return total

def part2(lines: list[str]):
    lines = parse(lines)
    total = 0
    for line in lines:
        parity = 1
        while(not all(v == 0 for v in line)):
            total += parity * line[0]
            parity *= -1
            line = differences(line)
    return total

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