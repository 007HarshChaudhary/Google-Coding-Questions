# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:22:15 2020

@author: Harsh Chaudhary
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=''
        if len(strs)==1:
            return strs[0]
        elif len(strs)==0:
            return prefix
        while len(strs)>1:
            str1 = strs.pop(0)
            str2 = strs.pop(0)
            prefix = commonPrefix(str1, str2)
            if prefix=="":
                return prefix
            else:
                strs.insert(0, prefix)

        return strs[0]
def commonPrefix(str1, str2):
    res=""
    i=0
    j=0
    while i<len(str1) and j<len(str2):
        if str1[i]==str2[i]:
            res+=str1[i]
        else:
            return res
        i+=1
        j+=1
    return res