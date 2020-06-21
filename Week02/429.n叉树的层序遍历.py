#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        data = []
        if root:
            self.helper([root], data)
        return data

    def helper(self, nodes, data):
        if nodes:
            all_child = []
            vals = []
            for node in nodes:
                vals.append(node.val)
                all_child.extend(node.children)
            if vals:
                data.append(vals)
            self.helper(all_child, data)
# @lc code=end

