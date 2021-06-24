# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:53:55 2020

@author: Harsh Chaudhary
"""
'''
You are given an array and you need to find number of tripets of 
indices  such that the elements at those indices are in geometric progression 
for a given common ratio r and i<j<k.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    total = 0
    for i in range(1, len(arr)-1):
        left = 0
        right = 0
        for ele in arr[: i]:
            if arr[i]//ele==r:
                left+=1
        for ele in arr[i+1: ]:
            if ele//arr[i]==r:
                right+=1
        total += left*right
    return total    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
############################################################################
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
from collections import Counter
def countTriplets(arr, r):
    result = 0
    right = Counter(arr)
    left = {}
    for i in arr:
        right[i] -= 1
        if i%r==0:
            result += right[i*r]*left.get(i//r, 0)
        left[i] = left.get(i, 0) + 1
    return result    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
