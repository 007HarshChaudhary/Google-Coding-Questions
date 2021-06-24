# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:23:46 2020

@author: Harsh Chaudhary
"""
dp = {}
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        
        ans = s[-1]
        dp[s[-1]] = None
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp[s[i:i+2]] = None
                ans = s[i:i+2]
            dp[s[i]]=None
        
        i=len(s)-3
        while i>=0:
            for j in range(i+2, len(s)):
                if s[i+1: j] in dp and s[i]==s[j]:
                    dp[s[i:j+1]]=None
                    if len(ans)<j-i+1:
                        ans = s[i:j+1]
            i-=1
        return ans
