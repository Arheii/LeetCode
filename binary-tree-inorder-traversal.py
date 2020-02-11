# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:04:07 2020
return inorder 
easy
https://leetcode.com/problems/binary-tree-inorder-traversal/
@author: Arh
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        
        
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)

        
print(Solution().inorderTraversal(root))