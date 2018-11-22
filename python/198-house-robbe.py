#!/usr/bin/env python
# encoding: utf-8


# 从左到右抢劫，对于每间房子，其当前最大抢劫财物数为：到前前个房子的最大财物数+当前屋子财物数 or
# 到前一个屋的最大财物数，选取二者的最大
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = {}
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[len(nums)-1]
