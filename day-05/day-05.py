import os
from timeit import default_timer as timer

DAY = "05"
TEST = True

NUMBER_OF_SEEDS = 100


def parse(lines: list[str]):
    seeds = [int(i) for i in lines[0].split(':')[1].split()]
    maps = []
    for line in lines[1:]:
        if len(line) == 0:
            continue
        elif line[-1] == ':':
            maps.append(list(range(NUMBER_OF_SEEDS)))
        else:
            dest_start, source_start, length = [int(i) for i in line.split()]
            for i in range(length):
                maps[-1][source_start + i] = dest_start + i

    return seeds, maps

def part1(lines: list[str]):
    results = []
    seeds, maps = parse(lines)
    for seed in seeds:
        for m in maps:
            seed = m[seed]
        results.append(seed)
    # print(results)
    return min(results)


def part2(lines: list[str]):
    pass

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