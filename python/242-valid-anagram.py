#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.check(s) == self.check(t)

    def check(self, s):
        exist = [0 for _ in range(26)]
        for i in s:
            exist[ord(i)-ord('a')] += 1
        return exist
