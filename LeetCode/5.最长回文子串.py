#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
# 之前的左右指针都是从两端向中间相向而行
# 而回文子串问题则是让左右指针从中心向两端扩展。
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 如果输入相同的 l 和 r，就相当于寻找长度为奇数的回文串，
        # 如果输入相邻的 l 和 r，则相当于寻找长度为偶数的回文串。
        def palinddrom(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 双指针，向两边展开
                l -= 1
                r += 1
            return s[l+1: r]
        res = ""
        for i in range(len(s)):
            str1 = palinddrom(s, i, i)
            str2 = palinddrom(s, i, i+1)
            res = str1 if len(str1) > len(res) else res
            res = str2 if len(str2) > len(res) else res
        return res

# @lc code=end
