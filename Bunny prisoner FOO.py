# -*- coding: utf-8 -*-
"""
Created on Sat May  2 14:24:41 2020

@author: Harsh Chaudhary
"""

def solution(x, y):
    # Your code here
    N = x+y-2
    ans = (N*(N+1))//2 + x
    return str(ans)