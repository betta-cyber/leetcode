#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        for i in xrange(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                sums = nums[l] + nums[r] + nums[i]
                if abs(sums - target) < abs(res - target):
                    res = sums
                if sums < target:
                    l = l + 1
                elif sums > target:
                    r = r - 1
                else:
                    return res
        return res
