#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)

        dp = triangle[n-1]

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j] = min( dp[j], dp[j+1] ) + triangle[i][j]

        return dp[0]
