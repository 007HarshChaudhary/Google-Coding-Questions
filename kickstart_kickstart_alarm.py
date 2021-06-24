# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:00:55 2020

@author: Harsh Chaudhary
"""

import math
M = 1000000007
#for t in range(int(input())):
#inputs = list(map(int, input().split()))
inputs = [3, 3, 1, 1, 1, 2, 1, 2, 9]
N = inputs[0]
k = inputs[1]
x1 = inputs[2]
y1 = inputs[3]
C = inputs[4]
D = inputs[5]
E1 = inputs[6]
E2 = inputs[7]
F = inputs[8]

result = ((x1+y1)*N*k)%M
gp_curr_sum = k
for i in range(2, N+1):
    temp_x1 = (C*x1 + D*y1 + E1)%F
    y1 = (D*x1 + C*y1 + E2)%F
    x1 = temp_x1
    A = (x1+y1)%F
    
    gp_curr_sum += i*(math.pow(i, k)-1)//(i-1)
    result += A*(N-i+1)*gp_curr_sum
    result %= M
print("Case #{}: {}".format(1, result))
        