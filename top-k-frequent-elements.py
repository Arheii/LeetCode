# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:04:07 2020
Возвращает k самых частых чисел в списке
Наверное, надо придумать алгоритм. но есть же most common ^^
easy
https://leetcode.com/problems/top-k-frequent-elements/
@author: Arh
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        return [x for x, count in Counter(nums).most_common(k)]