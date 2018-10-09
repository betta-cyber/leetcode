#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverse(head, None)

    def _reverse(self, node, pre):
        if not node:
            return pre
        n = node.next
        node.next = pre
        return self._reverse(n, node)
