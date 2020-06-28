#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def minDepth(self, root: TreeNode) -> int:
    #     if not root: return 0
    #     return self.helper(root, 1)
        
    # def helper(self, node, depth):
    #     if not node: return None
    #     if not node.left and not node.right: return depth
        
    #     left = self.helper(node.left, depth + 1)
    #     right = self.helper(node.right, depth + 1)
    #     if left and right: return min(left, right)
    #     if not right: return left
    #     return right
        
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
# @lc code=end

