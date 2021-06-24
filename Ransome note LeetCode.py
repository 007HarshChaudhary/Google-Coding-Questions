# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:19:06 2020

@author: Harsh Chaudhary
"""
'''
Given an arbitrary ransom note string and another string containing letters from all 
the magazines, write a function that will return true if the ransom note can be 
constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
'''

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)
        for ransomChar in counter1:
            if counter2[ransomChar]<counter1[ransomChar]:
                return False
        return True