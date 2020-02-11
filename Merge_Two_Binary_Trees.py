# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:49:42 2020
слить два бинарных дерева. если узлы были - то новый равен сумме
https://leetcode.com/problems/merge-two-binary-trees/
easy
@author: Arh
"""
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        if t1 == t2 == None:
            t0 = None
        elif t1 is None:
            t0 = t2
        elif t2 is None:
            t0 = t1
        else:
            t0 = TreeNode(t1.val + t2.val)
            t0.left = self.mergeTrees(t1.left, t2.left)
            t0.right = self.mergeTrees(t1.right, t2.right)
        return t0
    


t1 = TreeNode(1)
t2 = TreeNode(2)
sol = Solution().mergeTrees(t1, t2)
print(sol)
