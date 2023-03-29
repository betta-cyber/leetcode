# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if k == 0:
            return head

        t = head
        count = 1
        while t.next:
            t = t.next
            count += 1
        else:
            t.next = head

        for i in range(1, count-(k%count)):
            last = head
            head = head.next

        res = head.next
        head.next = None

        return res



s = Solution()
a = ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))
# while a:
    # print(a.val)
    # a = a.next
# [3,4,5,6]
# [5,6,3,4]

k = s.rotateRight(a, 2)

print("-------------")
while k:
    print(k.val)
    k = k.next
