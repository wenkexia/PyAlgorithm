import math
from typing import List

'''
https://leetcode.cn/contest/weekly-contest-316/problems/number-of-subarrays-with-gcd-equal-to-k/
6224. 最大公因数等于 K 的子数组数目 
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的子数组中元素的最大公因数等于 k 的子数组数目。

子数组 是数组中一个连续的非空序列。

数组的最大公因数 是能整除数组中所有元素的最大整数。

 
'''

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for idx, num in enumerate(nums):
            tmp = num
            for i in range(idx, len(nums)):
                tmp = math.gcd(tmp, nums[i])
                if tmp == k:
                    ans += 1
                elif tmp < k:    #为什么是公约数小于k时结束循环
                    break
        return ans



if __name__ =='__main__':
    nums = [9, 3, 1, 2, 6, 3]
    k = 3
    s =Solution()
    print(s.subarrayGCD(nums, k))

