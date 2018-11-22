#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            return self.change(root)
        else:
            return root

    def change(self, root):
        if root.left:
            self.change(root.left)
        if root.right:
            self.change(root.right)
        if root.left:
            tmp = root.right
            k = root.left
            root.left = None
            root.right = k
            while k.right:
                k = k.right
            k.right = tmp
