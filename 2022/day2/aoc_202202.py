# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    curated_input = []
    input = puzzle_input.split("\n")
    for line in input:
        curated_input.append(line.split(" "))
    return curated_input

def part1(data):
    """Solve part 1"""
    points = 0
    for match in data:
        if match[0] == 'A' and match[1] == 'X':
            points += 4
        elif match[0] == 'A' and match[1] == 'Y':
            points += 8
        elif match[0] == 'A' and match[1] == 'Z':
            points += 3
        elif match[0] == 'B' and match[1] == 'X':
            points += 1
        elif match[0] == 'B' and match[1] == 'Y':
            points += 5
        elif match[0] == 'B' and match[1] == 'Z':
            points += 9
        elif match[0] == 'C' and match[1] == 'X':
            points += 7
        elif match[0] == 'C' and match[1] == 'Y':
            points += 2
        elif match[0] == 'C' and match[1] == 'Z':
            points += 6
    return points
def part2(data):
    """Solve part 2"""
    points = 0
    for match in data:
        if match[0] == 'A' and match[1] == 'X':
            points += 0 + 3
        elif match[0] == 'A' and match[1] == 'Y':
            points += 3 + 1
        elif match[0] == 'A' and match[1] == 'Z':
            points += 6 + 2
        elif match[0] == 'B' and match[1] == 'X':
            points += 0 + 1
        elif match[0] == 'B' and match[1] == 'Y':
            points += 3 + 2
        elif match[0] == 'B' and match[1] == 'Z':
            points += 6 + 3
        elif match[0] == 'C' and match[1] == 'X':
            points += 0 + 2
        elif match[0] == 'C' and match[1] == 'Y':
            points += 3 + 3
        elif match[0] == 'C' and match[1] == 'Z':
            points += 6 + 1
    return points

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