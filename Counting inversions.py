# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:21:31 2020

@author: Harsh Chaudhary
"""

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def merge_invert(arr):
    inversions = 0
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[ :mid]
        R = arr[mid: ]

        inversions+=merge_invert(L)
        inversions+=merge_invert(R)

        i = j = k = 0

        while i < len(L) and j < len(R): 
            if L[i] <= R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j]
                inversions += mid-i 
                j+=1
            k+=1

        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return inversions
def countInversions(arr):
    return merge_invert(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        arr = map(int, raw_input().rstrip().split())

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
