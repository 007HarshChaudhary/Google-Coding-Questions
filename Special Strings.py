# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:47:42 2020

@author: Harsh Chaudhary
"""
'''
A string is said to be a special string if either of two conditions is met:

All of the characters are the same, e.g. aaa.
All characters except the middle one are the same, e.g. aadaa.
A special substring is any substring of a string which meets one of those criteria. 
Given a string, determine how many special substrings can be formed from it.
'''
#!/bin/python3
'''
import math
import os
import random
import re
import sys
from collections import Counter

# Complete the substrCount function below.
def check_pallindrome(arr):
    count = 0
    for string in arr:
        c = Counter(string)
        cond = True
        if len(string)%2==0:
            if len(c)!=1:
                cond = False
                
        elif len(string)%2==1:
            if len(c)>2:
                cond = False
                
            if len(c)==2 and string[len(string)//2]!=c.most_common()[1][0]:        
                cond = False
                
        if cond:
            count +=1
            
    return count

def substrCount(n, s):
    l = []
    count = 0
    for j in range(2, n+1):
        for i in range(n-j+1):
            l.append(s[i:j+i])
        count += check_pallindrome(l)
        l.clear()
    return count+n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.


def substrCount(n, s):
    ans=0
    l=[]
    curr = s[0]
    l.append([curr, 1])
    for i in range(1, n):
        if s[i]==curr:
            l[-1][1] += 1
        else:
            l.append([s[i], 1])
            curr = s[i]
    
    for item in l:
        ans += (item[1]*(item[1]+1))//2
    
    if len(l)>2:
        for i in range(1, len(l)-1):
            if l[i][1]==1 and l[i-1][0]==l[i+1][0]:
                ans += min(l[i-1][1], l[i+1][1])
    
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
