# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:04:07 2020
Возвращает k наименьший элемент с дерева
medium
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
@author: Arh
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        return sorted(tree_to_list(root))[k-1]
        

def tree_to_list(root):
    lst = []
    cash, root = [root], None
    while cash:
        if root is None:
            root = cash.pop()
        if root:
            lst.append(root.val)
            cash.append(root.right)
            root = root.left
    return lst
            
            
            
t1 = TreeNode(2)
t1.left = TreeNode(3)
t1.left.right = TreeNode(1)

print(Solution().kthSmallest(t1, 1))
