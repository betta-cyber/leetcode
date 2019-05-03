# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Recursive solution
"""

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = self.helper(root, [])
        return res
        
    def helper(self, root, res):
        if root:
            res.append(root.val)
            if root.left:
                self.helper(root.left, res)
            if root.right:
                self.helper(root.right, res)
        return res
