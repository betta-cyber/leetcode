#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        global res
        res = []
        if not root:
            return []
        self.dfs(root, "")

        return res


    def dfs(self, root, s):
        s = s+"->"+str(root.val)
        if not root.left and not root.right:
            global res
            res.append(s[2:])
        if root.left:
            self.dfs(root.left, s)
        if root.right:
            self.dfs(root.right, s)
