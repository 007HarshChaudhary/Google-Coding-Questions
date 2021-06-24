# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:15:08 2020

@author: Harsh Chaudhary
"""

class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        return power(x, n)
def power(x, n):
    ans = 1
    y = n
    n = abs(n)
    while(n>0):
        if (n&1)==1:
            ans*=x
        n = n>>1
        x *= x
    if y<0:
        ans = 1/ans
    return ans
print(Solution().myPow(2.0, -2))