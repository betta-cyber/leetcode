#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.helper(head, None)


    def helper(self, head, tail):
        if head == tail:
            return None
        if head.next == tail:
            return TreeNode(head.val)
        mid = head
        fast = head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            mid = mid.next

        node = TreeNode(mid.val)
        node.left = self.helper(head, mid)
        node.right = self.helper(mid.next, tail)
        return node
