#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 前序遍历二叉树
# 然后借助巧妙的#，相当于入队列
# 比较

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
