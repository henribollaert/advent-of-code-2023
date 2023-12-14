import os
from timeit import default_timer as timer

DAY = "05"
TEST = False

"""
Explicitly mapping everything won't work
"""

def parse(lines: list[str]) -> list[int]:
    pass

def part1(lines: list[str]) -> int:
    seeds = [int(i) for i in lines[0].split(':')[1].split()] # nog te verwerken seeds
    next_seeds = [] # seeds voor volgende stap
    for line in lines[2:]:
        if len(line) == 0:
            seeds.extend(next_seeds)  # any seeds that didn't match a map get mapped to themselves
            next_seeds = []
        elif line[-1] == ':':
            continue
        else:
            dest_start, source_start, length = [int(i) for i in line.split()]
            unmatched_seeds = []
            for seed in seeds:
                if source_start <= seed < source_start + length:
                    next_seeds.append(dest_start + seed - source_start)
                else:
                    unmatched_seeds.append(seed)
            seeds = unmatched_seeds
    seeds.extend(next_seeds)
    return min(seeds)


def part2(lines: list[str]):
    seed_ranges: list[range] = []
    line1 = [int (i) for i in lines[0].split(':')[1].split()]
    for i in range(len(line1) // 2):
        seed_ranges.append(range(line1[2 * i], line1[2 * i] + line1[2 * i + 1])) # nog te verwerken seed_ranges
    next_ranges: list[range] = [] # seed_ranges voor volgende stap

    for line in lines[2:]:
        if len(line) == 0:
            seed_ranges.extend(next_ranges)  # any ranges that didn't match a map get mapped to themselves
            next_ranges = []
        elif line[-1] == ':':
            continue
        else:
            dest_start, source_start, length = [int(i) for i in line.split()]
            unmatched_ranges: list[range] = []
            for seed_range in seed_ranges:
                overlap = range(max(seed_range.start, source_start), min(seed_range.stop, source_start + length))
                if len(overlap) > 0: # overlap niet nul -> mapping
                    next_ranges.append(range(dest_start + overlap.start - source_start, dest_start + overlap.stop - source_start))
                    if len(overlap) < len(seed_range): # overlap niet volledig: andere delen worden terug in huidge seed_range pool gestoken
                        if seed_range.start < source_start:
                            unmatched_ranges.append(range(seed_range.start, source_start))
                        if seed_range.stop > source_start + length:
                            unmatched_ranges.append(range(source_start + length, seed_range.stop))
                else: # geen overlap -> terug in de pool
                    unmatched_ranges.append(seed_range)
            seed_ranges = unmatched_ranges # pool update
    seed_ranges.extend(next_ranges) # nog de laatste stappen samenvoegen
    return min([r.start for r in seed_ranges])

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