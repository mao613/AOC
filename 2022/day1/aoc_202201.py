# aoc202001.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    curated_input = []
    input = puzzle_input.split('\n\n')
    for line in input:
        curated_input.append([int(x) for x in line.split()])
    return curated_input

def part1(numbers):
    """Solve part 1"""
    list_of_calories = []
    for calories in numbers:
        calories_sum = 0
        for calorie in calories:
            calories_sum += calorie
        list_of_calories.append(calories_sum)
    return max(list_of_calories)

def part2(numbers):
    """Solve part 1"""
    list_of_calories = []
    for calories in numbers:
        calories_sum = 0
        for calorie in calories:
            calories_sum += calorie
        list_of_calories.append(calories_sum)
    sorted_calories = sorted(list_of_calories, reverse = True)
    top3_sum = 0
    for x in sorted_calories[:3]:
        top3_sum += x
    return top3_sum

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        numbers = parse(puzzle_input)
        print(part1(numbers))
        print(part2(numbers))