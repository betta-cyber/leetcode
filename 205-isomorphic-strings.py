#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def dictful(s):
            res = {}
            used = []
            c = 0
            for i, v in enumerate(s):
                if v in used:
                    for key, value in enumerate(used):
                        if v == value:
                            c = key
                else:
                    c += 1
                    used.append(v)
                if v in res:
                    res[c].append(i)
                else:
                    res[c] = [i]
            return res

        return dictful(s)==dictful(t)
