#!/bin/python3
# https://www.hackerrank.com/challenges/counting-valleys/problem

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    elev        = 0
    ctr_val     = 0
    flg_start   = True
    flg_inval   = False

    # Iterate through the path string
    for stp in path:
        # What kind of step are we taking?
        if stp == "U":
            adj = 1
        if stp == "D":
            adj = -1
            
        # Are we at sea level?
        if elev == 0:
            # Have just started?
            if flg_start:
                # yes: adjust the elevation
                elev = elev + adj
                flg_start = False
                continue 

        # Are we coming out of a valley?
        if adj == 1 and elev == -1:  # stepping up to sea level
            ctr_val = ctr_val + 1
            elev = elev + adj
            continue 

        # Adjust the elevation given the step type ("up" or "down")
        elev = elev + adj

    return ctr_val
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
