#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False

        tmp_x = x
        tmp_list = []
        while tmp_x:
            tmp_list.append(tmp_x % 10)
            tmp_x = tmp_x / 10

        num = len(tmp_list)-1
        reverse = 0
        for i in tmp_list:
            reverse += i * pow(10, num)
            num -= 1

        if reverse == x:
            return True
        else:
            return False


# 当作字符串来处理
class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)
