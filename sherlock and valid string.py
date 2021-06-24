# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:22:34 2020

@author: Harsh Chaudhary
"""
'''
Sherlock considers a string to be valid if all characters of the string 
appear the same number of times. It is also valid if he can remove just 1 character at 1 index in 
the string, and the remaining characters will occur the same number of times. Given a string s, 
determine if it is valid. If so, return YES, otherwise return NO.
'''
#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the isValid function below.
def isValid(s):
    counter = Counter(s)
    l = sorted(counter.values())
    A = set(l[:-1])
    B = set(l[1: ])
    if len(A)==1 and (next(iter(A)) + 1 == l[-1] or next(iter(A))== l[-1]):
        return "YES"
    if len(A)==0:
        return "YES"
    if len(B)==1 and l[0]==1:
        return "YES"
    if len(B)==1 and next(iter(B)) == l[0] + 1:
        return 'YES'

    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
   