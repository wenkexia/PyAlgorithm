#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, x in enumerate(nums):
            if target - x in dic:
                return [dic[target - x], i]
            dic[x] = i
# @lc code=end

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s=Solution()

    print(s.twoSum(nums, target))