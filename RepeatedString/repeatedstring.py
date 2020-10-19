#!/bin/python3
# https://www.hackerrank.com/challenges/repeated-string/problem

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    num_a_str = s.count("a")                    # of times "a" is found in s
    num_whole_str = int(n/len(s))               # of times s is repeated in a repeating  
                                                # string of length n

    num_rem_chrs = int(n%len(s))                # of characters in the string "remander"
    num_a_rem    = s[:num_rem_chrs].count("a")  # of times "a" is found in remainder
                                                # substring of s

    # Return the total number of "a"'s found which is equal to:
    #    1. # of a's in the set of repeating strings
    #    2. # of a's in the remainder substring
    total_num_a  = num_a_str*num_whole_str + num_a_rem

    return total_num_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
