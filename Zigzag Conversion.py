# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:09:52 2020

@author: Harsh Chaudhary
"""

'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
    (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"


'''
s='PAYPALISHIRING'
numRows = 3
dp = [""]*numRows
index=0
i=0
j=1
i_inc = None
while(index<len(s)):
    if j>0: i_inc = 1
    elif j<0: i_inc = -1
    
    while (i>=0 and i<numRows and index<len(s)):
        dp[i] += s[index]
        index+=1
        i += i_inc
    if i>numRows-1: i=numRows-2
    if i<0: i=1
    j*=-1
ans = ""
for string in dp:
    ans += string
print(ans)
#############################################################
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==len(s) or numRows==1:
            return s

        dp = [""]*numRows
        index=0
        i=0
        i_inc=1
            
        while (i>=0 and i<numRows and index<len(s)):
            dp[i] += s[index]
            index+=1
            i += i_inc
            if i>numRows-1: 
                i=numRows-2
                i_inc*=-1
            elif i<0: 
                i=1
                i_inc*=-1
            
        
        ans = ""
        for string in dp:
            ans += string
        
        return ans