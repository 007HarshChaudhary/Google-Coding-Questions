# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:30:06 2020

@author: Harsh Chaudhary
"""
import math
def is_perfect_square(num):
    return math.sqrt(num)-math.floor(math.sqrt(num))==0
    
for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    sum_arr = [0]*n
    sum_arr[0] = arr[0]
    for i in range(1, n):
        sum_arr[i] = sum_arr[i-1]+arr[i]
        
    ans = 0    
    for i in range(n):

        for j in range(i, n):
            if i==0:
                curr_sum = sum_arr[j]
            else:
                curr_sum = sum_arr[j]-sum_arr[i-1]
            if curr_sum>=0 and is_perfect_square(curr_sum):
                ans+=1
    
    print("Case #{}: {}".format(t+1, ans))