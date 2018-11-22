#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            next = cur.next
            if cur.val == val:
                if pre:
                    pre.next = next
                else:
                    head = head.next
            else:
                if cur != head:
                    pre = cur
                else:
                    pre = head
            cur = cur.next
        return head
