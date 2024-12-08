'''
The engineers are trying to figure out which reports are safe. 
The Red-Nosed reactor safety systems can only tolerate levels that 
are either gradually increasing or gradually decreasing. So, a report
only counts as safe if both of the following are true:

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

Analyze the unusual data from the engineers. How many reports are safe?

'''

import argparse

def parse_args():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Process a file name.")

    # Add an argument for the file name
    parser.add_argument("filename", type=str, help="The name of the file to process.")

    # Parse the arguments
    args = parser.parse_args()

    # Access the filename
    filename = args.filename
    print(f"Processing file: {filename}")
    return args

def parse_file(filename: str):
    with open(filename, 'r') as file:
        data = file.readlines()
    return data

def rule_1(x, y, increasing):
    if increasing and x > y:
        return True 
    else:
        return False



def valid_line(line):
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
    x, y = 0, 1
    increasing = x < y 
    decreasing = x > y
    for i in range(len(line) - 1):
        rule1 = rule_1(line[x], line[y], increasing)
        rule2 = rule_2(line[x], line[y])
        if not (rule1 and rule2):
            return False
    return True

def solve(lines):
    for line in lines:
        split_line = line.split()
        if (valid_line(split_line))

def solve_pt2(lines):
    pass 

if __name__ == "__main__":
    # open the file
    args = parse_args()

    # parse the file data
    lines = parse_file(args.filename) 

    # solve the first part
    ans = solve(lines)

    # solve the second part
    ans2 = solve_pt2(lines)

    # print out answer
    print(f"Part 1: {ans}")
    print(f"Part 2: {ans2}")