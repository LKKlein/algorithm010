#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         data = []
#         self.helper(root, data)
#         return data

#     def helper(self, node: 'Node', data: List[int]):
#         if node:
#             data.append(node.val)
#             for child in node.children:
#                 self.helper(child, data)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack, res = [root], []
        while stack:
            data = stack.pop()
            if isinstance(data, Node):
                stack.extend(data.children[::-1] + [data.val])
            elif isinstance(data, int):
                res.append(data)
        return res
# @lc code=end

