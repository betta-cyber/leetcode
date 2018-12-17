# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.cur_sum = 0
        self.Helper(root)
        return root

    def Helper(self, root):
        if not root:
            return
        self.Helper(root.right)
        root.val += self.cur_sum
        self.cur_sum = root.val
        self.Helper(root.left)
