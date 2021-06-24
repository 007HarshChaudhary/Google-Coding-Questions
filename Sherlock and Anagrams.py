# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:45:59 2020

@author: Harsh Chaudhary
"""

'''
Two strings are anagrams of each other if the letters of one string can be rearranged to 
form the other string. Given a string, find the number of pairs of substrings of the string 
that are anagrams of each other.

'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import combinations

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    sum = 0
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        for j in b:
            sum += b[j]*(b[j]-1)//2
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
