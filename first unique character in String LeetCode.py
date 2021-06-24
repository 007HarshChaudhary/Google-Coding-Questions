# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:51:41 2020

@author: Harsh Chaudhary
"""
'''
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.
'''

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]]==1:
                return i
        return -1