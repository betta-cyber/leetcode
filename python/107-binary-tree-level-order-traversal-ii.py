#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        p = [root]
        ret = []
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
            # 仅仅在这里做了一个处理，插入改为头部
            ret.insert(0, res_list)
        return ret
