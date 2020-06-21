#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            data = stack.pop()
            if isinstance(data, TreeNode):
                stack.extend([data.right, data.left, data.val])
            elif isinstance(data, int):
                res.append(data)
        return res
# @lc code=end

