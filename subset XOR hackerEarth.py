# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:43:20 2020

@author: Harsh Chaudhary
"""

'''
Given a set S. Generate T, a set that contains all subsets of S minus the null set 
and calculate A, XOR sum of the set T.
S={1,2,3}
T={{1},{2},{3},{1,2},{1,3},{2,3} ,{1,2,3}}
A=XORiana of T .
XORiana of a set is defined as XOR of all the elements it contains.
'''
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
# Write your code here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dp={}
    res=0
    if n==1:
        print(arr[0])
    else:

        print(res) 