#!/usr/bin/env python
# encoding: utf-8

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = nums
        self.k = k
        # heapify 将常规列表转换为堆。 在结果堆中，最小的元素被推到索引位置0。但是其余的数据元素不一定被排序。
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            # heappop - 该函数返回堆中最小的数据元素。
            heapq.heappop(self.pool)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.pool) < self.k:
            # heappush - 这个函数在堆中添加一个元素而不改变当前堆。
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            # heapreplace函数总是删除堆中最小的元素，并在未被任何顺序修复的地方插入新的传入元素
            heapq.heapreplace(self.pool, val)
        return self.pool[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
