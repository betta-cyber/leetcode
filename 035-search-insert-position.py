#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m = len(nums)
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return m
        else:
            for i in range(0, m):
                if nums[i] == target:
                    return i
                elif nums[i] < target and nums[i+1] > target:
                    return i+1
