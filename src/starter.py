'''
<DESC>
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
    pass 

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