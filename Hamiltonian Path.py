# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 14:43:41 2021

@author: Harsh Chaudhary
"""
N, M = list(map(int, input().split()))
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))

graph = [[0 for j in range(N+1)] for _ in range(N+1)]
for u, v in edges:
    graph[u][v] = 1

def isSafe(v, pos):
    if graph[path[pos-1]][v] == 0:
        return False
    for i in range(1, pos):
        if path[i] == v:
            return False
    return True

def pathUtil(pos):
    if pos == N and isSafe(pos, pos):
        return True
    
    for v in range(1, N+1):
        if isSafe(v, pos) == True:
            path[pos] = v
            if pathUtil(pos+1) == True:
                return True
            path[pos] = -1
    print(path)
    return False
        
path = [-1]*(N+1)
for i in range(1, N+1):
    path[1] = i
    if pathUtil(2) == True:
        print(True)
        break
else: print(False)