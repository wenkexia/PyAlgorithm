#
# @lc app=leetcode.cn id=1605 lang=python
#
# [1605] 给定行和列的和求可行矩阵
#

# @lc code=start
class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        n,m = len(rowSum),len(colSum)
        matrix = [[0]*m for _ in range(n)]

# @lc code=end

rowSum = [5,7,10]
colSum = [8,6,8]

