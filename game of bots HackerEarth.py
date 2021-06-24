# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:45:32 2020

@author: Harsh Chaudhary
"""

'''
There are two kind of bots in the game BOT A and BOT B. Both are designed so as to 
move only in one direction in a 1-D array. Bot A can move towards left whereas bot B is 
constrained to move rightwards. Both are constrained to move only to the empty elements 
and one cannot jump over another bot. Now, a particular state of array can be represented 
with a string of A,B and # where A/B represents that BOT of kind A/B is sitting there and # 
represents an empty space.

For example: AA###B, represents an arena of length 5, where A sits at first two places, 
then three empty places and bot of kind B at last place. Here, B can be atmost 3 postitions 
leftwards and that too when both A do not move.

Input: First line of input contains an integer which is the number of test cases, then, 
t lines follow where each line contains two strings initial and final. where both strings 
consists of A,B and # representing a particular state. NOTE: initial and final string will 
be of same length

Output: For each test case print "Yes" if it is possible to move from initial state to 
final state else "No".
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
    initial, target = input().split()
    
    dp_initial = {'A':[], 'B':[]}
    for i in range(len(initial)):
        if initial[i] in ['A', 'B']:
            dp_initial[initial[i]].append(i)
    initial = initial.replace('#', '')

    dp_target = {'A':[], 'B':[]}
    for i in range(len(target)):
        if target[i] in ['A', 'B']:
            dp_target[target[i]].append(i)
    target = target.replace('#', '')

    bool_A = True
    A_1 = dp_initial['A']
    A_2 = dp_target['A']
    if len(A_1)!=len(A_2):
        bool_A = False
    else:
        for i in range(len(A_1)):
            if A_1[i]<A_2[i]:
                bool_A = False
                break
    
    bool_B = True
    B_1 = dp_initial['B']
    B_2 = dp_target['B']
    if len(B_1)!=len(B_2):
        bool_B = False
    else:
        for i in range(len(B_1)):
            if B_1[i]>B_2[i]:
                bool_B = False
                break
    if initial==target and bool_A and bool_B:
        print('Yes')
    else:
        print('No')
    
        
        
    
        
    