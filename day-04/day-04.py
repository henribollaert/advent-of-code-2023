import os
from timeit import default_timer as timer
from dataclasses import dataclass

DAY = "04"

@dataclass
class Card:
    number: int
    winning_numbers: list[int]
    my_numbers: list[int]
    instances: int = 1

    def matches(self) -> int:
        return sum([i in self.winning_numbers for i in self.my_numbers])

    def score(self) -> int:
        if self.matches() > 0:
            return 2 ** (self.matches() - 1)
        return 0

def parse(lines: list[str]) -> list[Card]:
    cards = []
    for nr, line in enumerate(lines):
        line = line.split(':')[1]
        cards.append(Card(
            nr + 1,
            [int (i) for i in line.split('|')[0].split()],
            [int (i) for i in line.split('|')[1].split()]
            ))
    return cards

def part1(lines: list[str]):
    return sum([card.score() for card in parse(lines)])

def part2(lines: list[str]):
    total_amount = 0
    cards = parse(lines)
    for nr, card in enumerate(cards):
        for i in range(card.matches()):
            cards[nr + i + 1].instances += card.instances
        total_amount += card.instances
    return total_amount


def main():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, f'input-{DAY}.txt'), 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    for nr, function in enumerate([part1, part2]):
        start = timer()
        result = function(lines)
        end = timer()
        print(f"Score for part {nr + 1}: {result} in {(end - start)*1000}ms.")


if __name__ == "__main__":
    main()