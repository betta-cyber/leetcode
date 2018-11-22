#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digits = {}
        for i in nums:
            digits[i] = digits.get(i, 0) + 1
            if digits[i] > len(nums)/2:
                return i


#  Moore Voting Algorithm
# 每次都找出一对不同的元素，从数组中删掉，直到数组为空或只有一种元素
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = count = 0
        for i in nums:
            if count == 0:
                major = i
                count = 1
            else:
                count += 1 if major == i else -1
        return major
