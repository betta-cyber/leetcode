#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_v = 0
        left = 0
        right = len(height)-1

        while left < right:
            k = min(height[left], height[right]) * (right - left)
            if k > max_v:
                max_v = k
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
        return max_v
