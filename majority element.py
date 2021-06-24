# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:32:18 2020

@author: Harsh Chaudhary
"""
'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always 
exist in the array.
'''

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for num in nums:
            if c[num]>len(nums)//2:
                return num