# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:15:02 2020

@author: Harsh Chaudhary
"""

for t in range(int(input())):
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    

    ans = 0
    for i in range(k-1, n):
        ok = True
        for j in range(1, k+1):
            if A[i+1-j]!= j:
                ok = False
                break
        if ok:
            ans+=1
    print("Case #{}: {}".format(t+1, ans))