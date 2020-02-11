# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:04:07 2020
Переворачивает связанный список
easy
https://leetcode.com/problems/reverse-linked-list/
@author: Arh
#"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        last = None
        while head:
            print(head.val)
            temp = head.next
            head.next, last = last, head
            head = temp
#            head.next, head  = head, head.next
        return last
            

t = ListNode(1)
t.next = ListNode(2)
t.next.next = ListNode(3)

a = Solution().reverseList(t)
print(a, a.next)