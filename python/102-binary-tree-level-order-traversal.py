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

    
    
## python3 

#我们可以想到最朴素的方法是用一个二元组 (node, level) 来表示状态，它表示某个节点和它所在的层数，每个新进队列的节点的 level 值都是父亲节点的 level 值加一。最后根据每个点的 level 对点进行分类，分类的时候我们可以利用哈希表，维护一个以 level 为键，对应节点值组成的数组为值，广度优先搜索结束以后按键 level 从小到大取出所有值，组成答案返回即可。

#考虑如何优化空间开销：如何不用哈希映射，并且只用一个变量 node 表示状态，实现这个功能呢？

#我们可以用一种巧妙的方法修改 BFS：

#首先根元素入队
#当队列不为空的时候
#求当前队列的长度 s
 
#依次从队列中取 s 个元素进行拓展，然后进入下一次迭代

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        quene = [root]
        results = []       
        while len(quene) > 0:
            result = []
            size = len(quene)
            for k in range(size):
                i = quene.pop(0)
                result.append(i.val)
                if i.left:
                    quene.append(i.left)
                if i.right:
                    quene.append(i.right)
            results.append(result)

        return results
