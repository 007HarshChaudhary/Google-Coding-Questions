# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:33:05 2020

@author: Harsh Chaudhary
"""
'''
We write the integers of A and B (in the order they are given) on two separate 
horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers 
A[i] and B[j] such that:

A[i] == B[j]
The line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting lines cannot intersect even at the endpoints: 
each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.
'''

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if A[i-1]==B[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
        print(dp)
        return dp[-1][-1]