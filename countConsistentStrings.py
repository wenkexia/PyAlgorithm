# -*- coding: utf-8 -*-

"""
@file: countConsistentStrings.py
@author: wenke
@software: PyCharm
@time: 2022/11/8 8:35
@Description:
"""

from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for i in words:
            if self.isequal(i,allowed):
                    ans += 1
        return ans
    def isequal(self,str1,allowed):
        for i in str1:
            if i not in allowed:
                return False
        return True
if __name__ == '__main__':
    s = Solution()
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    print(s.countConsistentStrings(allowed,words))
