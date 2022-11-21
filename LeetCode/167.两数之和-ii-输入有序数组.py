#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        left , right  = 0,len(numbers)-1
        while left<=right:
            m,n=numbers[left],numbers[right]
            if m+n==target:
                return [left+1,right+1]
            elif m+n>target:
                right-=1
            elif m+n<target:
                left+=1
        return []
# @lc code=end

