#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        if not root:
            return root
        p = [root]
        while p:
            node_list = []
            for i in range(0, len(p)):
                cur = p[i]
                if cur.left:
                    node_list.append(cur.left)
                if cur.right:
                    node_list.append(cur.right)

            if len(node_list) == 0:
                break
            for i in range(0, len(node_list)-1):
                node_list[i].next = node_list[i+1]
            node_list[-1].next = None

            p = node_list
