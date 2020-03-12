# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs的思路,维护一个self.paths, 分别对子节点进行遍历


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.paths = []
        self.dfs(root, [root.val], sum)
        return self.paths

    def dfs(self, root, res, target):
        if not root:
            return
        if sum(res) == target and root.left is None and root.right is None:
            self.paths.append(res)
        if root.left:
            self.dfs(root.left, res + [root.left.val], target)
        if root.right:
            self.dfs(root.right, res + [root.right.val], target)
