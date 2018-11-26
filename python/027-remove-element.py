#!/usr/bin/env python
# encoding: utf-8

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# 考虑到o(1)，故用双指针，进行前后互换
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start
