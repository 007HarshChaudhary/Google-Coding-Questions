# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:25:45 2020

@author: Harsh Chaudhary
"""
import math
for t_itr in range(int(input())):
    n, l = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    res = [None for i in range(l+1)]
    index = None
    for i in range(l-1):
        if arr[i]==arr[i+1]:
            pass
        else:
            index = i
    
    res[index+1] = math.gcd(arr[index], arr[index+1])
    
    for i in range(index, -1, -1):
        res[i] = arr[i]//res[i+1]
    
    for i in range(index+1, l):
        res[i+1] = arr[i]//res[i]
    
    STRING='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dict={}
    res_sorted = list(set(res))
    res_sorted.sort()
    for i in range(26):
        dict[res_sorted[i]] = STRING[i]
    
    op=''
    
    for i in res:
        op += dict[i]
    
    print('Case #{}: {}'.format(t_itr+1, op))