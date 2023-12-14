import os
from timeit import default_timer as timer
from enum import IntEnum, Enum, auto
from dataclasses import dataclass
from collections import Counter
from typing import Type

DAY = "07"
TEST = False

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

CARDS_J = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


class HandType(IntEnum):
    HIGH = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE = auto()
    FULL_HOUSE = auto()
    FOUR = auto()
    FIVE = auto()

@dataclass
class Hand:
    cards: str
    bid: int
    type: HandType | None = None

    def __post_init__(self):
        self.bid = int(self.bid)
        self.initalize_type()

class NoJokerHand(Hand):
    def initalize_type(self):
        if self.type is None:
            counter = Counter(self.cards)
            match len(counter):
                case 1:
                    self.type = HandType.FIVE
                case 2:
                    if max(list(counter.values())) == 4:
                        self.type = HandType.FOUR
                    else:
                        self.type = HandType.FULL_HOUSE
                case 3:
                    if max(list(counter.values())) == 3:
                        self.type = HandType.THREE
                    else:
                        self.type = HandType.TWO_PAIR
                case 4:
                    self.type = HandType.ONE_PAIR
                case 5:
                    self.type = HandType.HIGH
                case _:
                    raise ValueError(f"{self.cards} has an incorrect amount of cards.")
            


    def __lt__(self, other):
        if self.type == other.type:
            i = 0
            while(i < len(self.cards) and CARDS.index(self.cards[i]) == CARDS.index(other.cards[i])):
                i += 1
            return i != len(self.cards) and CARDS.index(self.cards[i]) < CARDS.index(other.cards[i])
        return self.type < other.type


def parse(lines: list[str], hand_type: Type[Hand]) -> list[Hand]:
    hands: list[Hand] = []
    for line in lines:
        hands.append(hand_type(*line.split()))
    return hands

def part1(lines: list[str]):
    sorted_hands = sorted(parse(lines, NoJokerHand))
    total_winnings = 0
    for i, hand in enumerate(sorted_hands):
        total_winnings += (i+1) * hand.bid
    return total_winnings

CARDS_J = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

@dataclass
class JokerHand(Hand):
    cards: str
    bid: int
    type: HandType | None = None

    def initalize_type(self):
        if self.type is None:
            nr_of_j = self.cards.count('J')
            if nr_of_j == 5:
                self.type = HandType.FIVE
            else:
                no_j = self.cards.replace('J', '')
                counter=Counter(no_j)
                # we can assume that all J's in a hand always take the same value
                # so we will add the nr_of_j's to the max character
                counter[counter.most_common(1)[0][0]] += nr_of_j
                match len(counter):
                    case 1:
                        self.type = HandType.FIVE
                    case 2:
                        if max(list(counter.values())) == 4:
                            self.type = HandType.FOUR
                        else:
                            self.type = HandType.FULL_HOUSE
                    case 3:
                        if max(list(counter.values())) == 3:
                            self.type = HandType.THREE
                        else:
                            self.type = HandType.TWO_PAIR
                    case 4:
                        self.type = HandType.ONE_PAIR
                    case 5:
                        self.type = HandType.HIGH
                    case _:
                        raise ValueError(f"{self.cards} has an incorrect amount of cards. Nr of J = {nr_of_j}")
            

    def __lt__(self, other):
        if self.type == other.type:
            i = 0
            while(i < len(self.cards) and CARDS_J.index(self.cards[i]) == CARDS_J.index(other.cards[i])):
                i += 1
            return i != len(self.cards) and CARDS_J.index(self.cards[i]) < CARDS_J.index(other.cards[i])
        return self.type < other.type

def part2(lines: list[str]):
    sorted_hands = sorted(parse(lines, JokerHand))
    total_winnings = 0
    for i, hand in enumerate(sorted_hands):
        total_winnings += (i+1) * hand.bid
    return total_winnings

def main():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, f'{"test" if TEST else "input"}-{DAY}.txt'), 'r')
    lines = [line.strip() for line in f.readlines()]
    f.close()

    # counter = Counter("Mary had a little lamb")
    # counter['M'] += 1
    # print(counter['M'])
    # print(counter.most_common(1))

    for nr, function in enumerate([part1, part2]):
        start = timer()
        result = function(lines)
        end = timer()
        print(f"Score for part {nr + 1}: {result} in {(end - start)*1000}ms.")


if __name__ == "__main__":
    main()