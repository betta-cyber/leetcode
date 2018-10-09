#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in m:
                return False
            else:
                m.add(n)
        else:
            return True
