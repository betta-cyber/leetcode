#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid1 = (left + right) / 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                left = mid2
            else:
                right = mid1
        return left

