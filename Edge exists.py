# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 14:21:24 2021

@author: Harsh Chaudhary
"""

N, M = list(map(int, input().split()))
graph = {}
for _ in range(M):
    a, b = list(map(int, input().split()))
    if a in graph:
        graph[a].add(b)
    else:
        graph[a] = set()
        graph[a].add(b)

def solve(a):
    return a[1] in graph[a[0]]
q = int(input())
for _ in range(q):
    print(solve(list(map(int, input().split()))))
