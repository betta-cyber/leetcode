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

    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return None
        tmp = []
        while head:
            tmp.append(head)
            head = head.next

        result = tmp.pop()
        current = result

        while tmp:
            k = tmp.pop(-1)
            current.next = k
            k.next = None
            current = k

        return result
