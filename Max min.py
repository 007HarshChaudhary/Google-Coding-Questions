# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:39:58 2020

@author: Harsh Chaudhary
"""
#!/bin/python3
'''You will be given a list of integers arr, and a single integer k. 
You must create an array of length k from elements of arr such that its unfairness is minimized. 
Call that array subarr. Unfairness of an array is calculated as:

    max(subarr)-min(subarr)
'''
import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    M=float('inf')
    for i in range(len(arr)-k+1):
        M = min(M, arr[i+k-1]-arr[i])

    return M
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
