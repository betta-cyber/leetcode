#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] == 0:
                for i in range(left,right):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                right -= 1
            else:
                left += 1
