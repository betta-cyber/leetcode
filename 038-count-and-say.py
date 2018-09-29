#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        last = "1"
        for i in range(n-1):
            tmp = last[0]
            count = 0
            re = ""
            for a in range(0, len(last)):
                if last[a] == tmp:
                    count = count + 1
                    if a == len(last)-1:
                        re = re + "%s%s" % (count, tmp)
                elif last[a] != tmp:
                    re = re + "%s%s" % (count, tmp)
                    if a < len(last) -1:
                        tmp = last[a]
                    count = 1
                    if a == len(last)-1:
                        re = re + "%s%s" % (count, last[a])
            last = re
        return last
