# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:04:01 2020
Перемешивает список. опять легкая хрень :/
medium?
https://leetcode.com/problems/shuffle-an-array/
"""

from random import shuffle

class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums
        

    def shuffle(self):
        ans = self.nums[:]
        shuffle(ans)
        return ans
    
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()