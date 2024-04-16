#!/usr/bin/env python3
# day_01.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse AoC input data."""
    return [str(line) for line in puzzle_input.split()]

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def part2(calibration_data):
    """Solve part 2."""
    conversion_data = []
    for data in calibration_data:
        new_string = []
        for i in range(len(data)):
            for digit in help_dict:
                if data.find(digit, i) == i:
                    new_string.append(help_dict[digit])
                    # data = data.replace(digit, help_dict[digit])
                else:
                    new_string.append(data[i])
                    # pass
        conversion_data.append(str(new_string))
        # conversion_data.append(data)
    data = part1(conversion_data)
    return data

def part1(conversion_data):
    calibrations = []
    for cal in conversion_data:
        calculations = []
        for val in cal:
            if val.isdigit():
                calculations.append(int(val))
        x = str(calculations[0]) + str(calculations[-1])
        calibrations.append(int(x))
    return sum(calibrations)

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
