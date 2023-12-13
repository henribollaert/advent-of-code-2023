import os
from timeit import default_timer as timer

DAY = "03"

def padd_grid(lines: list[str]) -> list[str]:
    schematic = ['.' * (len(lines[0]) + 2)]
    for line in lines:
        schematic.append('.' + line + '.')
    schematic.append('.' * (len(lines[0]) + 2))
    return schematic

def neighbouring(locs: list[tuple[int]]) -> list[tuple[int]]:
    """
    Returns a rectangle around the row given in the locs.
    """
    around_locs = []
    for row in [-1, 0, 1]:
        around_locs.append((locs[0][0] + row, locs[0][1] - 1)) # locatie ervoor
        around_locs.append((locs[-1][0] + row, locs[-1][1] + 1)) # locatie erachter
        if row != 0:
            for loc in locs:
                around_locs.append((loc[0] + row, loc[1]))
    return around_locs


def part1(lines: list[str]) -> str:
    start = timer()

    part_numbers = []
    schematic = padd_grid(lines)
    row = 1
    while(row < len(schematic) - 1):
        column = 1
        while(column < len(schematic[row]) - 1):
            if not schematic[row][column].isdigit():
                column += 1
            else: # we found a number
                locs = []
                number = 0
                while(column < len(schematic[row]) - 1 and schematic[row][column].isdigit()):
                    locs.append((row, column))
                    number = 10 * number + int(schematic[row][column])
                    column += 1
                # we have the location of the number, now check if its next to a symbol
                for around_loc in neighbouring(locs):
                    symbol = schematic[around_loc[0]][around_loc[1]]
                    if not symbol.isdigit() and symbol != '.':
                        part_numbers.append(number)
                        break

        row += 1

    end = timer()
    print(f'In {(end - start)*1000}ms.')

    return sum(part_numbers)

def part2(lines: list[str]) -> str:
    start = timer()

    gear_candidates = {} # candidate: list of adjacent numbers
    schematic = padd_grid(lines)
    row = 1
    while(row < len(schematic) - 1):
        column = 1
        while(column < len(schematic[row]) - 1):
            if not schematic[row][column].isdigit():
                column += 1
            else: # we found a number
                locs = []
                number = 0
                while(column < len(schematic[row]) - 1 and schematic[row][column].isdigit()):
                    locs.append((row, column))
                    number = 10 * number + int(schematic[row][column])
                    column += 1
                # we have the location of the number, now we add any surrounding gears to our dict with this as an adjacent number
                for around_loc in neighbouring(locs):
                    symbol = schematic[around_loc[0]][around_loc[1]]
                    if symbol == '*':
                        if around_loc not in gear_candidates:
                            gear_candidates[around_loc] = [number]
                        else:
                            gear_candidates[around_loc].append(number)

        row += 1
    # now we have all the candidates, we sum the ratios of those with exactly two adjacent parts
    result = 0
    for gear, adjacents_parts in gear_candidates.items():
        if len(adjacents_parts) == 2:
            result += adjacents_parts[0] * adjacents_parts[1]


    end = timer()

    print(f'In {(end - start)*1000}ms.')

    return result

def main():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, f'input-{DAY}.txt'), 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    print("Score for part 1:", part1(lines))
    print("Score for part 2:", part2(lines))

if __name__ == "__main__":
    main()