# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:06:18 2020

@author: Harsh Chaudhary
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the freqQuery function below.
def freqQuery(queries):
    res = Counter()
    res_2=Counter()
    ans=[]
    for q in queries:
        if q[0]==1:
            res_2[res[q[1]]] -= 1
            res[q[1]] += 1
            res_2[res[q[1]]] += 1
        elif q[0]==2:
            if res[q[1]]>0:
                res_2[res[q[1]]] -= 1
                res[q[1]] -= 1
                res_2[res[q[1]]] += 1 
        else:
            if res_2[q[1]]>0:
                ans.append(1)
            else:
                ans.append(0)
    return ans        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

