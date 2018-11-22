#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1

        while True:
            if numbers[left] + numbers[right] > target:
                right = right - 1
            if numbers[left] + numbers[right] < target:
                left = left + 1
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
