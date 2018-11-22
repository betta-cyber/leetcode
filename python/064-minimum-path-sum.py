#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for k in range(n):
                if i == 0 and k != 0:
                    grid[i][k] = grid[i][k-1] + grid[i][k]
                if i != 0 and k == 0:
                    grid[i][k] = grid[i-1][k] + grid[i][k]
                if i != 0 and k != 0:
                    grid[i][k] = min(grid[i-1][k], grid[i][k-1]) + grid[i][k]
        return grid[m-1][n-1]
