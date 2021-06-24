# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:23:36 2020

@author: Harsh Chaudhary
Dr. Patel has N stacks of plates. Each stack contains K plates. Each plate has a 
positive beauty value, describing how beautiful it looks.

Dr. Patel would like to take exactly P plates to use for dinner tonight. If he 
would like to take a plate in a stack, he must also take all of the plates above it 
in that stack as well.

Help Dr. Patel pick the P plates that would maximize the total sum of beauty values.
"""

for t in range(int(input())):
    n, k, p = list(map(int, input().split()))
    
    stacks = []
    for _ in range(n):
        stacks.append(list(map(int, input().split())))
    
    sum_stacks = [[0 for _ in range(k+1)] for _ in range(n)]
    for i in range(n):
        sum_stacks[i][0] = 0
        for j in range(1, k+1):
            sum_stacks[i][j] += sum_stacks[i][j-1]+stacks[i][j-1]
    
    dp = [[0 for _ in range(p+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(0, p+1):
            for x in range(0, min(j, k)+1):
                dp[i][j] = max(dp[i][j], dp[i-1][j-x]+sum_stacks[i-1][x])
    
    print("Case #{}: {}".format(t+1, dp[-1][-1]))
    