'''
Author: Arts 1184664659@qq.com
FilePath: 7.整数反转.py
Date: 2022-11-18 13:21:22
LastEditors: Arts 1184664659@qq.com
LastEditTime: 2022-11-18 15:54:25
Description:
'''
#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#
# 注意如果反转后整数超过 32 位的有符号整数的范围 [−2**31,  2**31 − 1] 返回 0。
# 2**31=2147483648
# @lc code=start


class Solution(object):
    # 转成字符串再反转
    def reverse1(self, x):
        if x > 0:
            return int(str(x)[::-1])
        elif x == 0:
            return 0
        else:
            return int("-" + str(x)[1:][::-1])

    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        rev = 0
        while x != 0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10  #取最后一位
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10

            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit

        return rev



# @lc code=end
