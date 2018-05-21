#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        curv = maxv = nums[0]
        for i in nums[1:]:
            curv = max(i+curv, i)
            maxv = max(curv, maxv)

        return maxv
