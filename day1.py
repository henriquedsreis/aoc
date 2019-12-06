"""
https://adventofcode.com/2019/day/1
Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?

Input:
https://adventofcode.com/2019/day/1/input
"""

import requests

#Part 2


def calc_fuel(mass: int):
    return int(mass/3)-2


def recur_calc_fuel(mass: int):
    if mass <= 8:
        return 0
    else:
        m = calc_fuel(mass)
        return m + recur_calc_fuel(m)


if __name__ == "__main__":
    # Getting input
    response = requests.get("https://adventofcode.com/2019/day/1/input", cookies={"session": "53616c7465645f5f66400c6ed0e0740fbcb8c7d87ea82f6c0166ffebf6b66dd9e75039a19233f6bf86359d6623c2fc39"})

    # Checking response
    if response.status_code == 200:
        print('Success!')
        print(str(response.text.count('\n')) + ' rows in payload!')
    else:
        print('Problem, status code ' + str(response.status_code))
        print(str(response.text))

    # List of strings
    input_str = response.text.split('\n')

    # Ugly assumption that there''s a newline in the end
    input_str.pop()

    # List of integers
    input_int = list(map(int, input_str))

    # debug
    #input_int = [12, 14, 1969, 100756]

    print(input_int)

    partial_output = list(map((lambda x: int(x/3)-2), input_int))
    # Output
    output_part1 = sum(partial_output)
    print('Part 1 output: ' + str(output_part1))

    """
    Part 2
    """
    print('Part 2')
    print(input_int)
    partial_output = list(map(recur_calc_fuel, input_int))

    print(partial_output)
    print(sum(partial_output))
