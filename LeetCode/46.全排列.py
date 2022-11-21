'''
Author: Arts 1184664659@qq.com
FilePath: 46.全排列.py
Date: 2022-11-18 16:33:47
LastEditors: Arts 1184664659@qq.com
LastEditTime: 2022-11-19 09:11:42
Description:
'''
#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
   def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def backtrack(first = 0):
        # 所有数都填完了
        if first == n:
            res.append(nums[:])
        for i in range(first, n):
            # 动态维护数组
            nums[first], nums[i] = nums[i], nums[first]
            # 继续递归填下一个数
            backtrack(first + 1)
            # 撤销操作
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    res = []
    backtrack()
    return res
# @lc code=end

