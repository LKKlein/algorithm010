#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    # 先查矩阵行，再查矩阵列
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        if target < matrix[0][0]: return False
        lower, upper = 0, len(matrix) - 1
        while lower <= upper:
            mid = (lower + upper) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                lower = mid + 1
            else:
                upper = mid - 1

        left, right = 0, len(matrix[upper]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[upper][mid] == target:
                return True
            elif matrix[upper][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    # 矩阵铺平进行二分查找
    # def searchMatrix(self, matrix, target):
    #     if not matrix or target is None:
    #         return False

    #     rows, cols = len(matrix), len(matrix[0])
    #     low, high = 0, rows * cols - 1
        
    #     while low <= high:
    #         mid = (low + high) / 2
    #         num = matrix[mid / cols][mid % cols]

    #         if num == target:
    #             return True
    #         elif num < target:
    #             low = mid + 1
    #         else:
    #             high = mid - 1
        
    #     return False
# @lc code=end

