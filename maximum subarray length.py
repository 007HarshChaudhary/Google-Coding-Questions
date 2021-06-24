# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:34:12 2020

@author: Harsh Chaudhary
Given a binary array, find the maximum length of a contiguous subarray with 
equal number of 0 and 1.
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res=0
        dp={0: -1}
        total=0
        for i in range(len(nums)):
            if nums[i]==1:
                total+=1
            else:
                total-=1
            if total in dp:
                res = max(res, i-dp[total])
            else:
                dp[total] = i
                
        return res