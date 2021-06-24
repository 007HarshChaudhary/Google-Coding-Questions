# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:48:50 2020

@author: Harsh Chaudhary
"""

'''
Given a positive integer num, output its complement number. 
The complement strategy is to flip the bits of its binary representation.
'''
class Solution:
    def findComplement(self, num: int) -> int:
        noOfBits = math.ceil(math.log2(num))
        ans = int(math.pow(2, noOfBits)-1-num)
        if ans>=0:
            return ans
        else:
            return int(math.pow(2, noOfBits)+ans)