#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        v = head
        while True:
            if v and v.next:
                tmp = v.val
                v.val = v.next.val
                v.next.val = tmp
                v = v.next.next
            else:
                break
        return head
