#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2:
            return s
        else:
            # 一分为二字符串
            return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])
