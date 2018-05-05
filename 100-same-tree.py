#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def bianli(t):
            if t is None:
                return ["#%"]
            return [t.val, "#"] + bianli(t.left) + bianli(t.right)

        return bianli(p) == bianli(q)
