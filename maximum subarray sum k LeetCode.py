# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:03:58 2020

@author: Harsh Chaudhary
"""
nums = [1,2,3]
k=3
res=0
sum_arr = [0]*(len(nums)+1)
for i in range(1, len(nums)+1):
    sum_arr[i] = sum_arr[i-1]+nums[i-1]
dp = {0: 1}
for i in range(len(nums)):
    if sum_arr[i+1]-k in dp:
        res+=dp[sum_arr[i+1]-k]
    dp[sum_arr[i+1]] = dp.get(sum_arr[i+1], 0)+1
        
print(res)  
#############################################
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        dp = {0: 1}
        s=0
        for i in range(len(nums)):
            s += nums[i]
            if s-k in dp:
                res+=dp[s-k]
            dp[s] = dp.get(s, 0)+1
                
        print(res)        
        return res