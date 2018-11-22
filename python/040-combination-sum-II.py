#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        global res
        res = []
        self.helper(sorted(candidates), target, 0, 0, [])
        return res


    def helper(self, candidates, target, c, cur, res_list):
        global res
        if cur == target:
            if res_list not in res:
                res.append(res_list)
        if cur < target:
            for i in range(c, len(candidates)):
                self.helper(candidates, target, i+1, candidates[i]+cur, res_list+[candidates[i]])


# 这个代码写的太垃圾了，用其他思路会比这个快很多，后续再更新
