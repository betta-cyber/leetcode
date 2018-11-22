#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        global res
        res = []
        self.helper(candidates, target, 0, [])
        return res


    def helper(self, candidates, target, cur, res_list):
        global res
        if cur == target:
            res.append(res_list)
        if cur < target:
            for i in candidates:
                if not res_list or i >= res_list[-1]:
                    self.helper(candidates, target, cur+i, res_list+[i])
