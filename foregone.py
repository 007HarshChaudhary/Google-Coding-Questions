# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:58:32 2020

@author: Harsh Chaudhary
"""
import math

def foregone(string):
    n = len(string)
    ans1 = 0.0
    ans2 = 0.0
    for i in range(n):
        if string[i] != '4':
            ans1 += int(string[i])*math.pow(10, n-i-1)
        else:
            ans1 += 2*math.pow(10, n-i-1)
            ans2 += 2*math.pow(10, n-i-1)
        
        
    print("Case #"+str(t_itr)+": ", int(ans1), int(ans2))

# =============================================================================
# def foregone(string):
#     ans1=''
#     ans2=''
#     for i in string:
#         if i=='4':
#             ans1 += '2'
#             ans2 += '2'
#         else:
#             ans1 += i
#             ans2 += '0'
#     
#     print('Case #{}: {} {}'.format(t_itr, int(ans1), int(ans2)))
# =============================================================================


t = int(input())
t_itr = 1
while t_itr<=t:
    n = input()
    foregone(n)
    t_itr+=1
