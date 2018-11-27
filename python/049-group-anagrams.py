#!/usr/bin/env python
# encoding: utf-8

from collections import Counter, defaultdict


# 这也太慢了一点吧。看看后期有什么可以优化的位置
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res_list = []
        res_dict = defaultdict()

        v = 0
        k = defaultdict()
        for i in strs:
            c = Counter()
            for s in i:
                c[s] += 1
            if c not in res_list:
                res_list.append(c)
                v += 1
                k[v] = c
                res_dict[v] = [i]
            else:
                for x,y in k.iteritems():
                    if c == y:
                        res_dict[x].append(i)

        return res_dict.values()


s = Solution()
a = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print a
