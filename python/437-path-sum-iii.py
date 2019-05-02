# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        count = 0
        res = self.dfs(root, count, sum)
        return res
    
    def dfs(self, root, count, sum):
        cc = self.caculate_sum(root, 0, sum)
        count += cc
        if root.left:
            l = self.dfs(root.left, 0, sum)
            count += l
        if root.right:
            r = self.dfs(root.right, 0, sum)
            count += r
        return count
            
    def caculate_sum(self, root, c, sum):
        count = 0
        if not root:
            return 0
        if root.val + c == sum:
            count += 1
        if root.left:
            l = self.caculate_sum(root.left, root.val + c, sum)
            count += l
        if root.right:
            r = self.caculate_sum(root.right, root.val + c, sum)
            count += r
        return count
