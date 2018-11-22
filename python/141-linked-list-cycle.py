#!/usr/bin/env python
# encoding: utf-8

# Floyd判圈算法 龟兔赛跑法
class Solution(object):
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
