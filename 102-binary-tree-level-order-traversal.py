#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        p, ret = [root], []
        while p:
            node_list = []
            res_list = []
            for node in p:
                res_list.append(node.val)
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
            p = node_list
            ret.append(res_list)
        return ret
