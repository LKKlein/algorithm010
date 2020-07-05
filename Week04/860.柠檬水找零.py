#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#
# [5,5,5,5,20,20,5,5,20,5]
# @lc code=start
# from collections import deque
class Solution:
    # def lemonadeChange(self, bills: List[int]) -> bool:
    #     changes = deque()
    #     for bill in bills:
    #         if bill == 5:
    #             changes.append(5)
    #         elif bill == 10:
    #             if changes and changes[-1] == 5:
    #                 changes.pop()
    #                 changes.appendleft(10)
    #             else:
    #                 return False
    #         else:
    #             if len(changes) >= 2 and changes[0] + changes[-1] == 15:
    #                 changes.popleft()
    #                 changes.pop()
    #             elif len(changes) >= 3 and changes[-1] + changes[-2] + changes[-3] == 15:
    #                 changes.pop()
    #                 changes.pop()
    #                 changes.pop()
    #             else:
    #                 return False
    #     return True

    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5: 0, 10: 0}
        for bill in bills:
            if bill == 10:
                if changes[5] >= 1:
                    changes[5] -= 1
                    changes[10] += 1
                else:
                    return False
            elif bill == 20:
                if changes[10] >= 1 and changes[5] >= 1:
                    changes[5] -= 1
                    changes[10] -= 1
                elif changes[5] >= 3:
                    changes[5] -= 3
                else:
                    return False
            else:
                changes[5] += 1
        return True
# @lc code=end

