#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = []
        tmp = ""
        res = ""
        for i in s:
            if i != " ":
                tmp = tmp+i
            if i == " ":
                if tmp:
                    str_list.append(tmp)
                tmp = ""
        if tmp:
            str_list.append(tmp)
        for k in reversed(str_list):
            res = res + k + ' '
        return res[:-1]


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))

