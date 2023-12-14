import os
from timeit import default_timer as timer
from collections import namedtuple
from math import lcm

DAY = "08"
TEST = False
TESTNR = "03"

Node = namedtuple("Node", "L R")


def parse(lines: list[str], get_starts: bool = False):
    directions = lines[0].replace('L', '0').replace('R', '1')
    nodes: dict[str, Node] = dict()
    starts: list[str] = []
    for line in lines[2:]:
        line = line.replace(' ', '')
        begin, dirs  = line.split('=')
        nodes[begin] = Node(*[dirs.strip('()').split(',')[i] for i in range(2)])
        if get_starts and begin[-1] == 'A':
            starts.append(begin)
    if get_starts:
        return directions, nodes, starts
    return directions, nodes

def part1(lines: list[str]):
    directions, nodes = parse(lines=lines)
    node = 'AAA'
    dir_it = 0
    while(node != 'ZZZ'):
        node = nodes[node][int(directions[dir_it % len(directions)])]
        dir_it += 1

    return dir_it

def part2(lines: list[str]):
    directions, nodes, starts = parse(lines=lines, get_starts=True)
    dir_it = 0
    lengths = []
    while(len(starts) > 0):
        nexts = []
        for node in starts:
            next_node = nodes[node][int(directions[dir_it % len(directions)])]
            if next_node[-1] == 'Z':
                lengths.append(dir_it + 1)
            else:
                nexts.append(next_node)
        starts = nexts
        dir_it += 1

    return lcm(*lengths)  # only works because the loops are same form '..A' nodes and '..Z' nodes, as well as multiples of the directions.


def main():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, f'{"test"+TESTNR if TEST else "input"}-{DAY}.txt'), 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    for nr, function in enumerate([part1, part2]):
        start = timer()
        result = function(lines)
        end = timer()
        print(f"Score for part {nr + 1}: {result} in {(end - start)*1000}ms.")


if __name__ == "__main__":
    main()