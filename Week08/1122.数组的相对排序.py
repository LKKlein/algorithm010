class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr_dict = {}
        for a in arr1:
            arr_dict[a] = arr_dict.get(a, []) + [a]
        result = []
        for a in arr2:
            result += arr_dict.pop(a)
        s = list(arr_dict.keys())
        for i in range(1, len(s)):
            if s[i] > s[i - 1]: continue
            for j in range(i):
                if s[j] > s[i]:
                    s.insert(j, s.pop(i))
                    break
        for a in s:
            result += arr_dict.pop(a)
        return result
