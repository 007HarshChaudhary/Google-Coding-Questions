# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:32:06 2020

@author: Harsh Chaudhary
"""

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        A.sort()
        B.sort()
        
        output = []
        
        for i in range(len(A)):
            j=0
            while j<len(B):
                temp = [A[i], B[j]]
                temp.sort()
                if temp[1][0]<=temp[0][1]:
                    output.append([max(temp[0][0], temp[1][0]), min(temp[0][1], temp[1][1])])
                j+=1
        print (output)
        return output
                    