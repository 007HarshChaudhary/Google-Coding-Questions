# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 22:00:26 2021

@author: Harsh Chaudhary
"""

from queue import PriorityQueue
N, M = list(map(int, input().split()))
graph = {}
visited = ["False"]*(N+1)
for _ in range(M):
    a, b, w = list(map(int, input().split()))
    graph[a] = graph.get(a, []) + [(w, b)]

dist = [float('inf')]*(N+1)
dist[1] = 0

q = PriorityQueue()
# cost, node
q.put((0, 1))

while not q.empty():
    distance, u = q.get()
    if distance > dist[u]: continue
    visited[u] = True
    for w, b in graph.get(u, []):
        if visited[b] == True: continue
        newDist = dist[u] + w
        if newDist < dist[b]:
            dist[b] = newDist
            q.put((newDist, b))

for i in range(2, N):
    if dist[i] == float('inf'):
        print(10**9, end=" ")
    else: print(dist[i], end=" ")
if dist[-1] == float('inf'):
    print(10**9)
else: print(dist[-1])