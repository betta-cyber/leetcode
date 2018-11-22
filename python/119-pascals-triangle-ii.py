#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [[1]*(k+1) for k in range(rowIndex+1)]
        for i in range(1, rowIndex+1):
            for j in range(1, i):
                res[i][j] = res[i-1][j] + res[i-1][j-1]
        return res[rowIndex]
