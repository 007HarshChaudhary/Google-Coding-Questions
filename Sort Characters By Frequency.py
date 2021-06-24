# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:31:15 2020

@author: Harsh Chaudhary
"""

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        op =''
        for char in counter.most_common():
            op+=char[0]*char[1]
        print (op)
        return op