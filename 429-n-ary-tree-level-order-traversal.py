#!/usr/bin/env python
# encoding: utf-8

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        # q means need loop node, one level one loop
        # ret means result list
        q, ret = [root], []
        while any(q):
            node_list = []
            child_list = []
            for node in q:
                node_list.append(node.val)
                if node.children:
                    for child in node.children:
                        child_list.append(child)
            ret.append(node_list)
            q = child_list
        return ret
