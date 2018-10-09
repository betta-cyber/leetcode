#!/usr/bin/env python
# encoding: utf-8

# 将其所有两边的数组都执行一次Best Time to Buy and Sell Stock I的解法，但这会带来O(N^2)的时间复杂度。实际上当计算prices[0]到prices[i]的最大收益时，我们已经计算过prices[0]到prices[i-1]的最大收益了，prices[0]到prices[i]的最大收益应该是当前卖出能获得的最大收益和prices[0]到prices[i-1]的最大收益中，二者较大的那个。我们可以利用这个之前计算的结果降低时间复杂度（不过代价是额外空间），所以需要把prices[0]到prices[i]的最大收益存在left[i]数组中。具体解法和I是一样的，也是维护一个前半段最小值。

#分别得出以i点为分割点，左半段最大收益的数组left，和右半段最大收益的数组right后，我们就可以遍历一遍这两个数组，找出最大的left+right组合。实际上，该解法就是将I的解法双向各执行一遍并记录结果。

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        left, right = [0 for _ in range(len(prices))], [0 for _ in range(len(prices))]
        min_l = prices[0]
        for i in range(1,len(prices)):
            min_l = min(prices[i], min_l)
            left[i] = max(prices[i] - min_l, left[i-1])
        max_r = prices[-1]
        for i in range(len(prices)-2, 0, -1):
            max_r = max(prices[i], max_r)
            right[i] = max(max_r - prices[i], right[i+1])
        res = 0
        for i in range(len(prices)):
            if (left[i]+right[i]) > res:
                res = left[i]+right[i]
        print left, right
        return res
