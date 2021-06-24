# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:56:49 2020

@author: Harsh Chaudhary
"""

'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first 
non-whitespace character is found. Then, starting from this character, takes an optional 
initial plus or minus sign followed by as many numerical digits as possible, and interprets 
them as a numerical value.

The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral 
number, or if no such sequence exists because either str is empty or it contains 
only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store 
integers within the 32-bit signed integer range: [−231,  231 − 1]. 
If the numerical value is out of the range of representable values, 
NT_MAX (231 − 1) or INT_MIN (−231) is returned.
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s)==0:
            return 0
        index = 0
        num = 0
        first = ''
        for i in range(len(s)):
            if s[i]!=' ':
                index = i
                break
        
        if s[index] not in ['+', '-'] and not s[index].isnumeric():
            return num
        else:
            first += s[index]
            index+=1
            while index<len(s):
                if s[index]==' ':
                    index+=1
                elif s[index].isnumeric():
                    if num is None:
                        num =0
                    num = num*10 + int(s[index])
                    index+=1
                else:
                    break
            if first=='+':
                return min(num, (2**31)-1)
            elif first=='-':
                return max(int(first+str(num)), -2**31)
            else:
                if num:
                    return min(int(first+str(num)), (2**31)-1)
                else:
                    return min(int(first), (2**31)-1)
                    
#################################################################################
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        digits = re.search('^(\s+)?[+|-]?\d+',str)
             
        numb = int(digits.group()) if digits else 0
        if numb < -2**31:
            return -2**31
        elif numb > 2**31 - 1:
            return 2**31 - 1
        else:
            return numb
