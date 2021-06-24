# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:26:50 2020

@author: Harsh Chaudhary
"""


class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        X = abs(x)
        while X>0:
            rem = X%10
            X //= 10
            rev = rev*10 + rem
        if x>0:
            return rev if rev<2**31 else 0
        else:
            return -1*rev if -1*rev>-2**31 else 0
#####################################################################
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if x<0:
            ans = int(s[0]+s[: 0: -1])
            if ans>2**31 or ans<-2**31:
                return 0
            return ans
        elif x==0:
            return 0
        else:
            ans = int(s[::-1])
            if ans>2**31 or ans<-2**31:
                return 0
            return ans