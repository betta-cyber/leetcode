#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n <= 0:
            return False
        while n>2:
            if n % 2 == 0:
                n /= 2
            else:
                return False
        return True
