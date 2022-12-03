# aoc_template.py

import pathlib
import sys

priorities_dic = {
    'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,
    'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,
    'v':22,'w':23,'x':24,'y':25,'z':26,'A':27,'B':28,'C':29,'D':30,'E':31,
    'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,
    'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,
    'Z':52
}

def parse(puzzle_input):
    """Parse input"""
    curated_input = []
    input = puzzle_input.split()
    for line in input:
        curated_input.append([x for x in line])
    return curated_input

def part1(data):
    """Solve part 1"""
    item_list = []
    for rucksacks in data:
        count = len(rucksacks)
        for x in rucksacks[:int(count/2)]:
            if x in rucksacks[int(count/2):]:
                item_list.append(x)
                break
    priorities_list = []
    for i in item_list:
        priorities_list.append(priorities_dic.get(i))
    return sum(priorities_list)

def part2(data):
    """Solve part 2"""
    badge_list = []
    i = 0
    while i <= len(data) - 2:
        for x in data[i + 0]:
            if x in data[i + 1]:
                if x in data[i + 2]:
                    badge_list.append(x)
                    break
        i += 3
    priorities_list = []
    for i in badge_list:
        priorities_list.append(priorities_dic.get(i))
    return sum(priorities_list)

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))