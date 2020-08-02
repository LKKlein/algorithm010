class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = list(sorted(intervals, key=lambda x: x[0]))
        p = 0
        while p < len(intervals) - 1:
            a, b = intervals[p], intervals[p + 1]
            if a[1] >= b[0]:
                intervals[p] = [a[0], max(a[1], b[1])]
                intervals.pop(p + 1)
            else:
                p += 1
        return intervals
