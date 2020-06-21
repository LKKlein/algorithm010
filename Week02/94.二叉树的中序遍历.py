#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     data = []
    #     self.inorder(root, data)
    #     return data
            
    # def inorder(self, root: TreeNode, data: List[int]):
    #     if root:
    #         self.inorder(root.left, data)
    #         data.append(root.val)
    #         self.inorder(root.right, data)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            data = stack.pop()
            if isinstance(data, TreeNode):
                stack.extend([data.right, data.val, data.left])
            elif isinstance(data, int):
                res.append(data)
        return res
# @lc code=end

