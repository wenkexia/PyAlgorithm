#
# @lc app=leetcode.cn id=1780 lang=python
#
# [1780] 判断一个数字是否可以表示成三的幂的和
#

# @lc code=start
class Solution(object):
    # 转换为三进制

    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 三进制 1 1 0 1 代表 1 * 3^3 + 1 * 3^2 + 0 * 3^1 + 1
        # 三进制 2 1 0 1 代表 2 * 3^3 + 1 * 3^2 + 0 * 3^1 + 1
        # 这样就有两个3^3，不符合题意, 所以判断三进制每一位有没有2即可
        while n > 0:
            if n % 3 == 2:
                return False
            n /= 3
        return True


# @lc code=end




# 回溯法
    def bdck(self, n: int) -> bool:
        arr = []
        x = 1
        t = 1
        while x <= n:
            arr.append(x)
            x = 3**t
            t += 1
        # 回溯

        k = len(arr)
        self.res = False

        def dfs(i, s):
            if self.res:
                return
            if i == k:
                if s == n:
                    self.res = True
                return
            dfs(i+1, s+arr[i])
            dfs(i+1, s)

        dfs(0, 0)
        return self.res