'''
Pair up the smallest number in the left list with the smallest 
number in the right list, then the second-smallest left number with the 
second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; 
you'll need to add up all of those distances.

PT2: 
Calculate a total similarity score by adding up each number in the left list 
after multiplying it by the number of times that number appears in the right list.
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

def solve(lines):
    # split into two lists
    left_list = []
    right_list = []
    for line in lines:
        stripped = line.rstrip().split()
        left_list.append(stripped[0])
        right_list.append(stripped[1])
    
    # sort the lists
    left_list.sort()
    right_list.sort()

    # zip the lists
    sum = 0
    for x, y in zip(left_list, right_list):
        # abs the differences
        sum += abs(int(x) - int(y)) 

    # return output
    return sum

def solve_pt2(lines):
    # split into two lists
    left_list = []
    right_list = []
    for line in lines:
        stripped = line.rstrip().split()
        left_list.append(stripped[0])
        right_list.append(stripped[1])

    # process the counts in the right list first
    counts = {}
    for value in right_list:
        counts[value] = counts.setdefault(value, 0) + 1

    # use those counts to sum the counts * num in the left list
    sum = 0
    for value in left_list:
        sum += counts.setdefault(value, 0) * int(value)

    # return the value
    return sum

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