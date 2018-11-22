#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        mid = (right - left) / 2 + left
        while right >= left:
            if mid * mid > x:
                right = mid
                mid = (right - left) / 2 + left
            if mid * mid <= x and (mid+1) * (mid+1) >= x :
                if (mid+1) * (mid+1) == x:
                    return mid+1
                else:
                    return mid
            if mid * mid <= x and (mid+1) * (mid+1) <x:
                left = mid
                mid = (right - left) / 2 + left
        return 0
