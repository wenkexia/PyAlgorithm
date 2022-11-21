#
# @lc app=leetcode.cn id=1768 lang=python
#
# [1768] 交替合并字符串
#

# @lc code=start
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        m,n = len(word1),len(word2)
        a=b=0
        ans = []
        while a<m or b<n:
            if a<m:
                ans.append(word1[a])
                a+=1
            if b<n:
                ans.append(word2[b])
                b+=1
        return ''.join(ans)
# @lc code=end

word1 = "abc"
word2 = "pqr"
s= Solution()
a= s.mergeAlternately(word1,word2)
print(a)