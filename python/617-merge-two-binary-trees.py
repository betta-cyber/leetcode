# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is not None and t2 is not None:
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            t1.val += t2.val
            return t1
        return t1 if t2 is None else t2
        
'''
合并两个二叉树当然就是同步遍历了，对于相同位置上的一对结点n1和n2，处理策略是：

若n1和n2都存在，则只需要保留其中一个结点（如n1），将另一结点的值加到此结点上即可（如n1.val += n2.val）。
若n1或n2任一不存在，则合并后的二叉树对应位置上的结点就是存在的那个了。
若n1和n2都不存在，则合并后仍不存在。
'''
