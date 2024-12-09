'''
The engineers are trying to figure out which reports are safe. 
The Red-Nosed reactor safety systems can only tolerate levels that 
are either gradually increasing or gradually decreasing. So, a report
only counts as safe if both of the following are true:

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

Analyze the unusual data from the engineers. How many reports are safe?

PT2: 
The Problem Dampener is a reactor-mounted module that lets the reactor 
safety systems tolerate a single bad level in what would otherwise be a safe report.
It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level 
from an unsafe report would make it safe, the report instead counts as safe.

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

def rule_1(prevIncreasing, curIncreasing):
    return prevIncreasing  == curIncreasing

def rule_2(x, y):
    diff = abs(x - y)
    if diff > 3 or diff < 1:
        return False
    return True

def valid_line(line):
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
    x, y = 0, 1
    prevIncreasing = int(line[x]) < int(line[y])
    for i in range(len(line) - 1):
        xval, yval = int(line[x]), int(line[y])
        curIncreasing = xval < yval 
        rule1 = rule_1(prevIncreasing, curIncreasing)
        rule2 = rule_2(xval, yval)
        if not (rule1 and rule2):
            return False
        x += 1
        y += 1
        prevIncreasing = curIncreasing
    return True

def solve(lines):
    sum = 0
    for line in lines:
        split_line = line.split()
        if (valid_line(split_line)):
            sum += 1

    return sum 

def valid_line_pt2(line):
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
    x, y = 0, 1
    isIncreasing = int(line[x]) < int(line[y])
    ruleEliminated = False
    for i in range(len(line) - 1):
        xval, yval = int(line[x]), int(line[y])
        stillIncreasing = xval < yval 
        # Check rule 1
        rule1 = rule_1(isIncreasing, stillIncreasing)
        # Check rule 2
        rule2 = rule_2(xval, yval)
        
        # Can we eliminate a value still?
        if (not rule1 or not rule2) and (not ruleEliminated):
            # Have we reached the end of the line?
            if y + 1 <= len(line) - 1:
                # Adjust variables to be next y value
                next_y_val = int(line[y+1])
                stillIncreasing = xval < next_y_val
                
                # check the rules again
                rule1 = rule_1(isIncreasing, stillIncreasing)
                rule2 = rule_2(xval, next_y_val)
                
                # if both rules don't pass by taking out the y value, then this line fails
                if not (rule1 and rule2):
                    return False
                else:
                    ruleEliminated = True 
            else:
                # if we can't remove this y value, then this line fails
                return False
        elif not rule1 and rule2:
            # if we have eliminated a rule and both rules aren't passing, then this line fails
            return False
        
        # increase book keeping variables
        x += 1
        y += 1
    return True


def solve_pt2(lines):
    sum = 0
    for line in lines:
        split_line = line.split()
        result = valid_line_pt2(split_line)
        if (result):
            sum += 1

    return sum 

if __name__ == "__main__":
    # open the file
    args = parse_args()

    # parse the file data
    lines = parse_file(args.filename) 

    # solve the first part
    ans = solve(lines)

    print("===========================================")

    # solve the second part
    ans2 = solve_pt2(lines)

    # print out answers 
    print(f"Part 1: {ans}")
    print("===========================================")
    print(f"Part 2: {ans2}")