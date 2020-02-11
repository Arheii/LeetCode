# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:04:01 2020
group anagrams together
medium
https://leetcode.com/problems/group-anagrams/
@author: Arh
"""
from itertools import groupby # Работает классно. но не группирует адекватно

class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        for s in strs:
            ss = ''.join(sorted(s))
            anagrams[ss] = anagrams.get(ss, []) + [s]
        return list(anagrams.values())
        

        
strs = ['eat', "tea", "tan", "ate", "nat", "bat"]
ans = Solution().groupAnagrams(strs)
print(ans)
#ab = {}
#for key, group in ans:
#    ab[key] = 
#    for x in group:
#        print(x, 'anagram for', key)
#    print('end group')
#    
#ans.