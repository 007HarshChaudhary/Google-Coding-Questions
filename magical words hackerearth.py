# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:27:18 2020

@author: Harsh Chaudhary
"""
'''
Queen of westeros is known for her dragons and magic. 
To control her dragons she speaks random but powerful words. The strength of her 
words can be predicted by a strange rule. Rule : Strength of a word is sum of square 
of size of palindromic substrings in the word. To recall the definition of palindrome, 
palindrome is a word which reads same when read forward and backward. For example, word 
"abaa" has 6 palindromic substrings. "aba","aa","a","b","a","a" with sizes 3,2,1,1,1,1 
respectively. Their squares are 9,4,1,1,1,1. Hence total strength is 17. Given a queens 
word ind its strength.
'''
def fun(s, l, r):
    global res
    while l>=0 and r<len(s):
        if s[l]==s[r]:
            res+=(r-l+1)**2
            l-=1
            r+=1
        else:
            break

# Write your code here
t=int(input())
for _ in range(t):
    s = input()
    # dp={}
    # for i in range(len(s)-1):
    #     dp[s[i]]=dp.get(s[i], 0)+1
    #     if s[i]==s[i+1]:
    #         dp[s[i:i+2]] = dp.get(s[i:i+2] ,0)+1
    # dp[s[-1]] = dp.get(s[-1], 0)+1

    # i=len(s)-3

    # while i>=0:
    #     for j in range(i+2, len(s)):
    #         if s[i]==s[j] and s[i+1:j] in dp:
    #             dp[s[i:j+1]] = dp.get(s[i:j+1] ,0)+1
    #     i-=1
    # res=0
    # for key in dp:
    #     res+= dp[key]*(math.pow(len(key), 2))
    # print(int(res))
    res=0
    for i in range(len(s)):
        fun(s, i, i)
        fun(s, i, i+1)
    print(res)