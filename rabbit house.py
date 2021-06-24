# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:04:30 2021

@author: Harsh Chaudhary
"""

from queue import PriorityQueue
T = int(input())
t = 1
while t <= T:
    res = 0
    rows, cols = list(map(int, input().split()))
    grid = []
    for i in range(rows):
        grid.append(list(map(int, input().split())))
    
    lookup = {}
    heap = PriorityQueue()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] not in lookup:
                lookup[grid[r][c]] = {(r,c)}
            else:
                lookup[grid[r][c]].add((r,c))
            heap.put(-grid[r][c])      
    
    def utility(r, c):
        global res
        res += peak - grid[r][c] - 1
        heap.put(1-peak)
        lookup[grid[r][c]].discard((r,c))
        if peak-1 not in lookup:
            lookup[peak-1] = {(r,c)}
        else:
            lookup[peak-1].add((r,c))   
        
    while not heap.empty():
        peak = heap.get()*-1
        while len(lookup[peak]) > 0:
            r, c = lookup[peak].pop()
            if r-1 >=0 and grid[r-1][c] < peak:
                utility(r-1, c)
            if r+1 < rows and grid[r+1][c] < peak:
                utility(r+1, c)
            if c-1 >=0 and grid[r][c-1] < peak:
                utility(r, c-1)
            if c+1 < cols and grid[r][c+1] < peak:
                utility(r, c+1)          
            
            
                
                
    print("Case #{}: {}".format(t, res))
    t += 1