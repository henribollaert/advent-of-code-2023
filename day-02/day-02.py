import os
from timeit import default_timer as timer
from dataclasses import dataclass

DAY = "02"

@dataclass
class Game:
    idnr: int
    red: int = 0
    green: int = 0
    blue: int = 0

    def __le__(self, other) -> bool:
        return self.red <= other.red and self.green <= other.green and self.blue <= other.blue
    
    def power(self) -> int:
        return self.red * self.green * self.blue



def parse_line(line: str) -> Game:
    game = Game(int(line.split()[1].strip(':')))
    for s in line.split(':')[1].split(';'):
        for subset in s.split(','):
            match subset.split()[1]:
                case 'red':
                    game.red = max(game.red, int(subset.split()[0]))
                case 'green':
                    game.green = max(game.green, int(subset.split()[0]))
                case 'blue':
                    game.blue = max(game.blue, int(subset.split()[0]))
                case _:
                    raise ValueError(f"{subset.split()[1]} is not a colour")
    return game

def part1(lines: list[str]) -> int:
    start = timer()

    bag = Game(idnr=0, red = 12, green = 13, blue = 14)
    result = 0
    for line in lines:
        game = parse_line(line.strip())
        if game <= bag:
            result += game.idnr
    end = timer()

    print(f'In {(end - start)*1000}ms.')

    return result

def part2(lines: list[str]) -> int:
    start = timer()

    result = 0
    for line in lines:
        result += parse_line(line.strip()).power()
    end = timer()

    print(f'In {(end - start)*1000}ms.')

    return result

def main():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    f = open(os.path.join(__location__, f'input-{DAY}.txt'), 'r')
    lines = f.readlines()
    f.close()

    print("Score for part 1:", part1(lines))
    print("Score for part 2:", part2(lines))

if __name__ == "__main__":
    main()