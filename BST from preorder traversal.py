# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:32:38 2020

@author: Harsh Chaudhary
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        i=0
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        i+=1
        while i<len(preorder):
            temp = None
            
            while len(stack)>0 and preorder[i]>stack[-1].val:
                temp = stack.pop()
            
            if temp is None:
                temp = stack[-1]
                temp.left = TreeNode(preorder[i])
                stack.append(temp.left)
            else:
                temp.right = TreeNode(preorder[i])
                stack.append(temp.right)
            
            i+=1
        queue = [root]
        output = []
        while len(queue)>0:
            temp = queue.pop(0)
            if temp:
                output.append(temp.val)
                if temp.left is not None and temp.right is not None:
                    queue.append(temp.left)
                    queue.append(temp.right)
                elif temp.left is None and temp.right is not None:
                    queue.append(None)
                    queue.append(temp.right)
                elif temp.right is None and temp.left is not None:
                    queue.append(temp.left)
                    queue.append(None)
            else:
                output.append(None)
        print(output)
        return root