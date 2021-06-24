# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 09:55:09 2020

@author: Harsh Chaudhary
"""
s='MCMXCIV'
dp = {'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}
res=0
i=len(s)-1
if len(s)==1:
    print(dp[s[i]])
else:
    while i>0:
        if (s[i-1]=='I' and s[i] in ['V', 'X']) or (s[i-1]=='X' and s[i] in ['L', 'C']) or (s[i-1]=='C' and s[i] in ['D', 'M']):
            res+= dp[s[i]]-dp[s[i-1]]
            i-=2
        else:
            res+=dp[s[i]]
            i-=1
    if i!=-1:
        res+=dp[s[0]]
    print(res)