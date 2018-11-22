#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = s[::-1]
        leng = len(s)
        if leng == 1:
            return s
        if leng == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        dp = [[0 for _ in range(leng)] for _ in range(leng)]
        max_d = 0
        left = 0
        right = 0
        # 构造空dp,反转字符，求最长公共子串
        for i in range(0, leng):
            if s[i] == rs[0]:
                dp[i][0] = 1
        for j in range(0, leng):
            if s[0] == rs[j]:
                dp[0][j] = 1
        for i in range(1, leng):
            for j in range(1, leng):
                if s[i] == rs[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_d:
                    # 求出最长公共子串后，并不一定是回文串，需要判断该字符串倒置前的下标和当前的字符串下标是不是匹配
                    if leng-(i+1-dp[i][j]) == j+1:
                        max_d = dp[i][j]
                        left = i
                        right = j

        return s[left-max_d+1:left+1]


# Manacher‘s Algorithm 待补充, 时间复杂度o(n)
