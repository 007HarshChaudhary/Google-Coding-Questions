# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:21:04 2020

@author: Harsh Chaudhary
There are N houses for sale. The i-th house costs Ai dollars to buy. You have a budget of B 
dollars to spend.

What is the maximum number of houses you can buy?
"""

for t in range(int(input())):
    N, B = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    arr.sort()
    i=0
    while B and i<N:
       if arr[i]>B:
           break
       else:
           B = B-arr[i]
       i+=1
   
    print('Case #{}: {}'.format(t+1, i))