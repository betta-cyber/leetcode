# -*- coding: utf-8 -*-


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # new 一个 dict
        # 然后for nums，判断是否在dict中，然后加一
        # 然后排序，取前n
        occurence = dict()

        for n in nums:
            if n in occurence:
                occurence[n] = (n, occurence[n][1]+1)
            else:
                occurence[n] = (n, 1)

        vals = occurence.values()

        vals.sort(key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(vals[i][0])

        return res
