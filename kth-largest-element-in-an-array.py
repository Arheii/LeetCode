# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:04:01 2020
Если к где-то в центре списка, просто его сортируем. если близко к краям -
пользуемся самопальным поиском чтобы не сортировать всё
medium
https://leetcode.com/problems/kth-largest-element-in-an-array/
@author: Arh
"""

from bisect import bisect, bisect_left

class Solution:
    def findKthLargest(self, nums, k):
        n = len(nums)
        sqrt_n = n ** 0.5
        if sqrt_n < n < (n - sqrt_n) and n > 100:
            return sorted(nums)[n - k]
        elif k <= n // 2:
            temp = [-x for x in reversed(sorted(nums[:k]))]
            print('way2', temp, k)
            for x in nums[k:]:
                if temp[-1] > -x:
                    temp.pop()
                    temp.insert(bisect(temp, -x), -x)
            return -temp.pop()
        elif k > n // 2:
            k = n - k + 1
            temp = sorted(nums[:k])
            print('way3', temp, k)
            for x in nums[k:]:
                if temp[-1] > x:
                    temp.pop()
                    temp.insert(bisect(temp, x), x)
            return temp.pop()
                    

ans1 = Solution().findKthLargest([3,2,1,5,6,4], 2)
print(ans1)
ans2 = Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print(ans2)