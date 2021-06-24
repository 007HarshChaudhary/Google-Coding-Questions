# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:55:36 2020

@author: Harsh Chaudhary
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack=[]
        while True:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k-=1    
            if k==0:
                return root.val
            root = root.right
        