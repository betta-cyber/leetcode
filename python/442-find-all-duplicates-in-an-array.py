#!/usr/bin/env python
# encoding: utf-8
# 同448,使用正负数进行判断,若已经为负数则加入res


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        for n in nums:
            j = abs(n) - 1
            if nums[j] > 0:
                nums[j] = -nums[j]
            elif nums[j] < 0:
                res.append(abs(n))
        return res
