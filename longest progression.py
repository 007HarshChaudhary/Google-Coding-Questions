# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:54:34 2021

@author: Harsh Chaudhary
"""

T = int(input())
t = 1
while t <= T:
    res = [1]
    n = int(input())
    s = list(map(int, input().split()))
    
    res = [0 for i in range(n)]
    for i in range(1, n):
        res[i] = abs(s[i]-s[i-1])
    
    print("Case #{}: {}".format(t, res))
    t += 1