import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #check if the array is empty or only has 1 element 
    if len(ar) <= 1: 
        return 0
    #create a hash table
    pairs_table = dict()
    #create a variable for pairs
    pairs = 0

    for i in ar:
        if i not in pairs_table: 
            pairs_table[i] = 1
        else: 
            pairs_table[i] += 1
            if pairs_table[i] % 2 == 0: 
                pairs += 1
    
    return pairs