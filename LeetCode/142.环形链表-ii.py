'''
Author: Arts 1184664659@qq.com
FilePath: 142.环形链表-ii.py
Date: 2022-11-20 10:35:20
LastEditors: Arts 1184664659@qq.com
LastEditTime: 2022-11-20 11:08:37
Description:
'''
#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        #重新指向头结点
        fast = head
        #快慢指针同步前进，相交点就是环起点
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


# @lc code=end

