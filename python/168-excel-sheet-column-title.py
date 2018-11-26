#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res_list = []
        res = ""
        while n > 0:
            s = n % 26
            if s == 0:
                s = 26
            res_list.append(s)
            n = (n-s)/26
        for i in reversed(res_list):
            res += str(unichr(i+64))
        return res
