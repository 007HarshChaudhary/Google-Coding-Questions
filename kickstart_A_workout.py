# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:05:15 2020

@author: Harsh Chaudhary
"""

import math
for t in range(int(input())):
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    
    lb=1
    rb = A[-1]-A[0]
    while(lb<rb):
        mb = (rb+lb)//2
        k2=0
        for i in range(1, n):
            k2 += math.ceil((A[i]-A[i-1])/mb)-1
            
        if k2>k:
            lb = mb+1
        elif k2<=k:
            rb = mb

    print("Case #{}: {}".format(t+1, lb))
            
    
        
    
        