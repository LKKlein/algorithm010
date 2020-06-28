#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    #     return self.helper(root)

    # def helper(self, node, lower=float("-inf"), upper=float("inf")):
    #     if not node:
    #         return True
        
    #     val = node.val
    #     if val <= lower or val >= upper:
    #         return False

    #     if not self.helper(node.left, lower, val):
    #         return False
        
    #     if not self.helper(node.right, val, upper):
    #         return False
        
    #     return True

    # def isValidBST(self, root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #     stack = [root]
    #     last = float("-inf")
    #     while stack:
    #         data = stack.pop()
    #         if isinstance(data, TreeNode):
    #             stack.extend([data.right, data.val, data.left])
    #         if isinstance(data, int):
    #             if data > last:
    #                 last = data
    #             else:
    #                 return False
    #     return True

    def isValidBST(self, root: TreeNode) -> bool:
        self.last_val = float("-inf")
        return self.helper(root)

    def helper(self, node):
        if not node:
            return True

        if not self.helper(node.left):
            return False

        if node.val <= self.last_val:
            return False
        else:
            self.last_val = node.val

        if not self.helper(node.right):
            return False
        
        return True
# @lc code=end

