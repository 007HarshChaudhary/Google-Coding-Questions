# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 12:41:44 2021

@author: Harsh Chaudhary
"""
import math
from bisect import bisect_left
from collections import Counter

n = int(input())
arr = [0]*21
for i in range(1, 21):
    arr[i] = (int(math.pow(2, 2*i)) + arr[i-1] + 2)


group = bisect_left(arr, n)
noOfTerm = n - arr[group-1]

print(noOfTerm)
