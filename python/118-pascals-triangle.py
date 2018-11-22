#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]*(k+1) for k in range(numRows)]
        for i in range(numRows):
            for j in range(numRows):
                if i >= j and i!=0 and j != 0 and i != j:
                    res[i][j] = res[i-1][j] + res[i-1][j-1]
        return res
