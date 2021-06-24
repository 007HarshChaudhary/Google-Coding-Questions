# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:18:14 2020

@author: Harsh Chaudhary
"""
'''
You're given strings J representing the types of stones that are jewels, and S 
representing the stones you have.  Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".
'''

from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = Counter(S)
        res=0
        for jewel in J:
            res+= counter.get(jewel, 0)
        return res