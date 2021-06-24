# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:39:02 2020

@author: Harsh Chaudhary
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    dp = [[0 for i in range(len(s1)+1)] for j in range(len(s1)+1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp)):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[-1][-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

