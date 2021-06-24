# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:06:26 2020

@author: Harsh Chaudhary
"""

'''
Thanh wants to paint a wonderful mural on a wall that is N sections long. Each section of the wall 
has a beauty score, which indicates how beautiful it will look if it is painted. Unfortunately, 
the wall is starting to crumble due to a recent flood, so he will need to work fast!

At the beginning of each day, Thanh will paint one of the sections of the wall. 
On the first day, he is free to paint any section he likes. On each subsequent day, he 
must paint a new section that is next to a section he has already painted, since he does 
not want to split up the mural.

At the end of each day, one section of the wall will be destroyed. It is always a section 
of wall that is adjacent to only one other section and is unpainted (Thanh is using a waterproof 
paint, so painted sections can't be destroyed).

The total beauty of Thanh's mural will be equal to the sum of the 
beauty scores of the sections he has painted. Thanh would like to guarantee that, 
no matter how the wall is destroyed, he can still achieve a total beauty of at least B. 
What's the maximum value of B for which he can make this guarantee?
'''
import math
for i in range(int(input())):
    n = int(input())
    beauty_scores = input()
    int_scores = [0]*n
    for i in range(n):
        int_scores[i] = int(beauty_scores[i])
    if n==2:
        print("Case #{}: {}".format(i+1, max(int_scores)))
    else:
            
        total_sections_that_can_be_painted = math.ceil(n/2)
        dp = [0]*n
        dp[0] = int_scores[0]
        
        for i in range(1, len(dp)):
            dp[i] = dp[i-1] + int_scores[i]
        
        value = dp[total_sections_that_can_be_painted-1]
        for i in range(1, n-total_sections_that_can_be_painted+1):
            value = max(value, dp[i+total_sections_that_can_be_painted-1] - dp[i-1])
    
        print("Case #{}: {}".format(i+1, value))