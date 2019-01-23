#!/usr/bin/env python
# encoding: utf-8
# 标志位法：用正负标志位，区分出现的元素和未出现的元素


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for n in nums:
            j = abs(n) - 1
            if nums[j] > 0:
                nums[j] = -nums[j]
        index = 0
        for v in nums:
            index += 1
            if v > 0:
                res.append(index)
        return res
