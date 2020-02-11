# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:04:01 2020
возвращает дерево, где сначала нечетные ноды, затем четные 1 - 3 - 5 - 2 - 4
medium?
https://leetcode.com/problems/odd-even-linked-list/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        if head is None:     return
        even = even_head = head.next
        odd = head
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = even.next
            if odd is not None:
                even.next = odd.next
                even = odd.next
            else:
                break
            
        odd.next = even_head

        
        
        
        
        
        
        
t1 = ListNode(1)
t1.next = ListNode(2)
t1.next.next = ListNode(3)

print(Solution().oddEvenList(t1))
print(t1.next.val)