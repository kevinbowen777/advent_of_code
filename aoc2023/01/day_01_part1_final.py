#!/usr/bin/env python3
# day_01.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse AoC input data."""
    return [str(line) for line in puzzle_input.split()]


def part1(calibration_data):
    """Solve part 1."""
    calibrations = []

    for cal in calibration_data:
        calculations = []
        for val in cal:
            if val.isdigit():
                calculations.append(int(val))
        x = str(calculations[0]) + str(calculations[-1])
        calibrations.append(int(x))
    return sum(calibrations)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        calibration_data = parse(puzzle_input)
        print(part1(calibration_data))
