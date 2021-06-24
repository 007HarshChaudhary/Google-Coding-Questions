# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 12:58:10 2021

@author: Harsh Chaudhary
"""

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
# Write your code here
N, M = list(map(int,input().split()))
edge_list = []

parent = [-1]*(N+1)

for _ in range(M):
    a, b, w = list(map(int, input().split()))
    edge_list.append((a, b, w))

def find(i):
    while parent[i] != -1:
        i = parent[i]
    return i

def union(a, b):
    parent[a] = b

def isSafe(a, b):
    x = find(a)
    y = find(b)
    if x == y:
        return False
    else:
        union(x, y)
        return True

edge_list.sort(key = lambda x: -x[2])
res = 0
i = 0
while i<N-1:
    a, b, w = 0, 0, 0
    if len(edge_list) > 0:
        a, b, w = edge_list.pop()    
    if isSafe(a, b):
        res += w
        i += 1

print(res)