#!/usr/bin/env python
# encoding: utf-8

# 可以说是最慢的Accepted了，需要优化

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        topk = []
        for n in nums:
            if len(topk) < k:
                topk = self.addlist(topk, n)
            else:
                if n > topk[-1]:
                    topk = self.addlist(topk, n)[:-1]
        return topk[-1]


    def addlist(self, l, k):
        if l:
            start = l[-1]
            n = []
            while l and l[-1] < k:
                v = l.pop()
                n.append(v)
            l.append(k)
            while n:
                l.append(n.pop())
        else:
            l.append(k)
        return l


class Solution(object):
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
