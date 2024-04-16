#!/usr/bin/env python3

"""

day_00.py
Advent of Code template

"""

import pathlib
import sys


def parse(puzzle_input):
    """Parse AoC input data."""
    return [str(line) for line in puzzle_input.split()]


def part2(data):
    """Solve Part 2."""
    return data


def part1(data):
    """Solve Part 1."""
    return data


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
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
