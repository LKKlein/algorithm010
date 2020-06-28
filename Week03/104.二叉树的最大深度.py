#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    #     res = []
    #     self.helper(root, 1, res)
    #     return max(res)

    # def helper(self, node, depth, res):
    #     if not node:
    #         res.append(depth - 1)
    #         return
        
    #     self.helper(node.left, depth + 1, res)
    #     self.helper(node.right, depth + 1, res)

    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0 
        left_height = self.maxDepth(root.left) 
        right_height = self.maxDepth(root.right) 
        return max(left_height, right_height) + 1 
# @lc code=end

