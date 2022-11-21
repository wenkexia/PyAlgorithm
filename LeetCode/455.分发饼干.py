'''
Author: Arts 1184664659@qq.com
FilePath: 455.分发饼干.py
Date: 2022-11-16 20:45:13
LastEditors: Arts 1184664659@qq.com
LastEditTime: 2022-11-17 19:33:00
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
        g.sort()
        s.sort( )
        m,n=len(g)-1,len(s)-1
        i = j = count = 0
        while(m>=0 and n>=0):
            if g[m]<=s[n]:
                count+=1
                m-=1
                n-=1
            elif g[m]>s[n]:
                m-=1
        return count



# @lc code=end



if __name__ == "main":
    # g= [10,9,8,7]
    # s=[5,6,7,8]
    # a=Solution()
    # print(a.findContentChildren(g,s))
    # def findContentChildren():




