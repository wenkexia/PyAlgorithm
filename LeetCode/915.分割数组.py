#
# @lc app=leetcode.cn id=915 lang=python
#
# [915] 分割数组
#

# @lc code=start
from typing import List
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        #维护一个左边最大值，一个当前最大值
        max_l=max_curr = nums[0]
        #维护一个左边的位置
        curr_pos = 0
        for i in range(1,n):
            max_curr  =max(max_curr,nums[i])
            if nums[i]<max_l:
                max_l ,curr_pos = max_curr,i
        return curr_pos+1
        
# @lc code=end


nums = [5,0,3,8,6]
s =Solution()
print(s.partitionDisjoint(nums))