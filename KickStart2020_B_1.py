# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:34:37 2020

@author: Harsh Chaudhary
"""

for t in range(int(input())):
    n, d = list(map(int, input().split()))
    A = list(map(int, input().split()))
    
    
    lb = 0
    rb = d

    while lb<rb:
        mb = (lb+rb+1)//2
        ans = mb
        for x in A:
            if ans%x!=0:
                ans += x-ans%x
        if ans<=d:
            lb = mb
        else:
            rb = mb-1
    print("Case #{}: {}".format(t+1, lb))
    