# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.res = None
        self.dfs(root, p, q)
        
        return self.res
        
    def dfs(self, root, p, q):
        
        if not root:
            return 0
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        mid = (root == p or root == q)
        
        if mid + left + right >= 2:
            self.res = root
        return left or right or mid
        

# 对二叉树做后序遍历，回溯
# 回溯时： 捕获mid，即当前节点是否为p或q；
# 当 left right mid 三个中有两个为True时，说明当前节点是最近的公共节点，记录至res；
# 返回值： 左子树或右子树或当前节点中包含p或q；
# 最终，返回最近公共节点res。
