#!/bin/python3
# https://www.hackerrank.com/challenges/sock-merchant/problem

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    mp_sock  = {}
    ctr_pair = 0

    # Iterate through the passed array
    for clr in ar:
        # Is this sock color in our working map?
        if clr not in mp_sock.keys():
            # No: add the sock color as a key
            mp_sock[clr] = 1
            continue 

        # Color is already in the map - we have now found a sock pair
        # Increase the pair count
        ctr_pair = ctr_pair + 1

        # Delete the current color key - so we can identify the next pair
        del mp_sock[clr]

    # Done iterating... return the current counter value
    return ctr_pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
