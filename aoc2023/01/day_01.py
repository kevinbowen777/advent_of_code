#!/usr/bin/env python3

"""

Advent of Code
Day 1: Trebuchet?!.

"""

import pathlib
import sys

def parse(puzzle_input):
    """Parse AoC input data.
    Load input text.

    >>> puzzle_input = '''1abc2
    ... pqr3stu8vwx
    ... a1b2c3d4e5f
    ... treb7uchet'''
    >>> parse(puzzle_input)
    ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
    """
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
    """
    Part Two.
    Convert words of numbers to digits.

    >>> part2(['1abc2'])
    12
    >>> part2(['pqr3stu8vwx'])
    38
    >>> part2(['a1b2c3d4e5f'])
    15
    >>> part2(['treb7uchet'])
    77
    >>> part2(['two1nine'])
    29
    >>> part2(['eightwothree'])
    83
    >>> part2(['abcone2threexyz'])
    13
    >>> part2(['xtwone3four'])
    24
    >>> part2(['4nineeightseven2'])
    42
    >>> part2(['zoneight234'])
    14
    >>> part2(['7pqrstsixteen'])
    76
    >>> part2(['nineight'])
    98
    """
    conversion_data = []
    for data in calibration_data:
        new_string = []
        for i in range(len(data)):
            for digit in help_dict:
                if data.find(digit, i) == i:
                    new_string.append(help_dict[digit])
                else:
                    new_string.append(data[i])
        conversion_data.append(str(new_string))
    data = part1(conversion_data)
    return data

def part1(conversion_data):
    """
    Part One.

    >>> values1 = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
    >>> part1(values1)
    142
    >>> values2 = [
    ... 'two1nine',
    ... 'eightwothree',
    ... 'abcone2threexyz',
    ... 'xtwone3four',
    ... '4nineeightseven2',
    ... 'zoneight234',
    ... '7pqrstsixteen'
    ... ]
    >>> part2(values2)
    281
    """
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
    """
    Get calibration value.

    >>> solve('1abc2')
    (12, 12)
    >>> solve('pqr3stu8vwx')
    (38, 38)
    >>> values = ['1abc2', 'pqr3stu8vwx']
    >>> part2(values)
    50
    """
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
