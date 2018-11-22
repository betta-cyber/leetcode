#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        width = len(matrix[0])
        height = len(matrix)
        dp = [[0 for i in range(width)] for j in range(height)]

        ans = 0
        for i in range(width):
            dp[0][i] = int(matrix[0][i])
            ans = max(ans, dp[0][i])
        for j in range(height):
            dp[j][0] = int(matrix[j][0])
            ans = max(ans, dp[j][0])

        for j in range(1, height):
            for i in range(1, width):
                if matrix[j][i] != "0":
                    dp[j][i] = min(dp[j-1][i-1], min(dp[j-1][i], dp[j][i-1])) + 1
                    ans = max(ans, dp[j][i])

        return ans * ans
