# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:04:07 2020
delete node from linked list
easy
https://leetcode.com/problems/delete-node-in-a-linked-list/
@author: Arh
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val, node.next = node.next.val, node.next.next
        
       
t1 = ListNode(1)
t1.next = ListNode(2)
t1.next.next = ListNode(3)           


print(Solution().deleteNode(t1.next))
print(t1.next.val)