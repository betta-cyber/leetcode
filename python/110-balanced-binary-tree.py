#!/usr/bin/env python
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 遍历每个节点，判断当前节点的左右height是否小于等于1
# height的计算也是通过递归的方式，获取最大的，遍历一遍加1

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
