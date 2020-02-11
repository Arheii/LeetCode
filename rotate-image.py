# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:04:01 2020
return only one duplicate n in list(n+1)
time O(n^2). memory O(n)
Существует более красивое решение за O(n).
Использовать идею, что мы обязательно зациклимся, если будет переходить
по значениям как по индексам
medium
https://leetcode.com/problems/find-the-duplicate-number/
@author: Arh
"""

class Solution:
    def findDuplicate(self, nums):
        """памяти О(1), времени O(nlogn)
        Главная идея - смотрим кол-во цифр больше и меньше медианы. повторяем
        """
        print('__'* 10)
        n = len(nums)
        ld, rd = 0, n   # Левые и правые границы поиска
        while ld < rd:
            med = ld + (rd - ld) // 2 # медиана для поиска
            lcount = rcount = 0
            for x in nums:
                if ld < x < med:
                    lcount += 1
                elif med < x < rd:
                    rcount += 1
            print(ld, med, rd, ', lcount =', lcount, ', rcount =', rcount)
            if lcount > med - ld - 1:
                rd = med
            elif rcount > rd - med - 1:
                ld = med
            else:
                return med
        return ld
        

        
nums1 = [1,3,4,2,2]
nums2 = [3,1,3,4,2]
ans1 = Solution().findDuplicate(nums1)
ans2 = Solution().findDuplicate(nums2)
print(ans1, ans2)
