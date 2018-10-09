#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        # haven't sold anything can't do worse than that
        max_profit = 0
        # highest possible price
        min_buy = float('inf')
        for p in prices:
            # possible new profit = if we sell at p - what we bought at min
            max_profit = max(max_profit,p-min_buy)
            # if it is cheaper why not buy here instead and see if we can do better
            # than the current max_profit sometime later
            min_buy = min(min_buy,p)
        return max_profit


# 双指针法
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        if prices:
            min_v = prices[0]
            for i in range(len(prices)):
                if prices[i] < min_v:
                    min_v = prices[i]
                if prices[i] - min_v > res:
                    res = prices[i] - min_v
        return res
