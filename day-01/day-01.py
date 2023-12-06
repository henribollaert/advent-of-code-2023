import os
from timeit import default_timer as timer

DAY = "01"

def parse(lines: list[str]):
    pass

def findletter(line: str) -> str:
    for letter in line:
            if letter.isnumeric():
                return letter

def part1(lines: list[str]):
    start = timer()
    result = sum([int(findletter(line) + findletter(line[::-1])) for line in lines])
    end = timer()

    print(f'In {(end - start)*1000}ms.')

    return result

digits = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]

def part2(lines: list[str]):
    start = timer()
    result = 0
    for line in lines:
        i = 0
        first_digit = 0
        while i < len(line):
            if line[i].isnumeric():
                first_digit = int(line[i])
                break
            if line[max(0, i-2): i+1] in digits:
                first_digit = digits.index(line[max(0, i-2): i+1]) + 1
                break
            if line[max(0, i-3): i+1] in digits:
                first_digit = digits.index(line[max(0, i-3): i+1]) + 1
                break
            if line[max(0, i-4): i+1] in digits:
                first_digit = digits.index(line[max(0, i-4): i+1]) + 1
                break
            i+=1
        last_digit = 0
        i = len(line) - 1
        while i >= 0:
            if line[i].isnumeric():
                last_digit = int(line[i])
                break
            if line[i: min(len(line), i + 3)] in digits:
                last_digit = digits.index(line[i: min(len(line), i + 3)]) + 1
                break
            if line[i: min(len(line), i + 4)] in digits:
                last_digit = digits.index(line[i: min(len(line), i + 4)]) + 1
                break
            if line[i: min(len(line), i + 5)] in digits:
                last_digit = digits.index(line[i: min(len(line), i + 5)]) + 1
                break
            i-=1
        print(first_digit*10 + last_digit)
        result += first_digit*10 + last_digit     
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