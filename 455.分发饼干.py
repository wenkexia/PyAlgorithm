'''
Author: Arts 1184664659@qq.com
FilePath: 455.分发饼干.py
Date: 2022-11-16 20:45:13
LastEditors: Arts 1184664659@qq.com
LastEditTime: 2022-11-16 22:51:27
Description:
'''
#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()
        ans = 0
        j = 0

        for i in range(len(g)):
            if j==len(s):
                return ans
            if j<len(s) and g[i]<=s[j]  :
                ans+=1

            j+=1

        return ans

# @lc code=end

if __name__ == "main":
    g= [10,9,8,7]
    s=[5,6,7,8]
    a=Solution()
    print(a.findContentChildren(g,s))