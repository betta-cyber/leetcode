#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        global res, count
        res = 0
        count = 0
        self.dfs(root, k)
        return res

    def dfs(self, root, k):
        if root.left:
            self.dfs(root.left, k)
        global count, res
        count += 1
        if k == count:
            res = root.val
        if root.right:
            self.dfs(root.right, k)
