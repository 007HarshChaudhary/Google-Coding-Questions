# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:12:34 2020

@author: Harsh Chaudhary
"""

def solution(n):
    # Your code here
    memo = [[0 for i in range(n + 1)] for j in range(n + 1)]
    memo[0][0] = 1

    for i in range(1, n + 1):
        for j in range(0, n + 1):
            m[i][j] = m[i - 1][j]
            if j >= i:
                m[i][j] += m[i - 1][j - i]
    
    ans = m[n][n] - 1
    return ans