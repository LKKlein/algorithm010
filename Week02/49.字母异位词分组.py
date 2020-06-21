#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for s in strs:
            ss = "".join(self.qsort_v2(list(s)))
            if ss not in data:
                data[ss] = []
            data[ss].append(s)
        return list(data.values())

    def qsort(self, arr):
        # 非原地排序
        if len(arr) <= 1:
            return arr
        base, left, right = arr.pop(), [], []
        for item in arr:
            if item <= base:
                left.append(item)
            else:
                right.append(item)
        return self.qsort(left) + [base] + self.qsort(right)

    def qsort_v2(self, arr):
        # 原地排序
        self.mqsort(arr, 0, len(arr) - 1)
        return arr

    def mqsort(self, arr, left, right):
        if left < right:
            pivot_key = self.partition(arr, left, right)
            self.mqsort(arr, left, pivot_key - 1)
            self.mqsort(arr, pivot_key + 1, right)

    def partition(self, arr, left, right):
        pivot_value = arr[left]

        while left < right:
            while left < right and arr[right] >= pivot_value:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= pivot_value:
                left += 1
            arr[right] = arr[left]
        arr[left] = pivot_value
        return left

# @lc code=end

