#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        return max(self.rob_row(nums[1:]), self.rob_row(nums[:-1]))

    def rob_row(self, nums):
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i] = max(res[i-1], res[i-2] + nums[i])

        return res[-1]
