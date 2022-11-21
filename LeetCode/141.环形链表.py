'''
Author: Arts 1184664659@qq.com
FilePath: 141.环形链表.py
Date: 2022-11-19 23:07:56
LastEditors: Arts 1184664659@qq.com
LastEditTime: 2022-11-20 10:31:23
Description:
'''
#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast!=None and fast.next!=None:
            #慢指针走一步，快指针走两步
            slow = slow.next
            fast = fast.next.next
            #快慢指针相遇，说明含有环
            if slow == fast:
                return True
        return False





# @lc code=end

