# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:40:43 2020
return max depth three
easy
https://leetcode.com/problems/maximum-depth-of-binary-tree/
@author: Arh
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))