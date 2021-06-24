# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:12:12 2020

@author: Harsh Chaudhary
"""

nmk = input().split()

n = int(nmk[0])

m = int(nmk[1])

k = int(nmk[2])

track = []

for _ in range(k):
    track.append(list(map(int, input().rstrip().split())))

s = 0
i=0
while i<len(track)-1:
    if track[i][0]==track[i+1][0] and track[i][2]>=track[i+1][1]:
        a = track.pop(i)
        b = track.pop(i)
        if len(track)==0:
            track.append([a[0], min(a[1], b[1]), max(a[-1], b[-1])])
        else:
            track.insert(i, [a[0], min(a[1], b[1]), max(a[-1], b[-1])])
    
    else:
        i+=1
for t in track:
    s += abs(t[2]-t[1])+1
print (n*m-s)
