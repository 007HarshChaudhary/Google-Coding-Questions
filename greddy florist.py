# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:03:22 2020

@author: Harsh Chaudhary
"""
'''Given the size of the group of friends, the number of flowers 
they want to purchase and the original prices of the flowers, determine the 
minimum cost to purchase all of the flowers.'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    temp_count = 0
    cost = 0
    for i in range(len(c)):
        temp_count = i//k
        cost += (temp_count + 1)*c[i]
    return cost
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
