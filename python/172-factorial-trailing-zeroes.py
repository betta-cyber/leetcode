#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        while n:
            n = n / 5
            sum += n
        return sum
