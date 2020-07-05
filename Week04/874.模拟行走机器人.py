#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y, di = 0, 0, 0
        maxDistance = 0
        obstacles = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -2: di = (di - 1) % 4
            elif cmd == -1: di = (di + 1) % 4
            else:
                for i in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacles:
                        x += dx[di]
                        y += dy[di]
                    else:
                        break
                maxDistance = max(maxDistance, x * x + y * y)
        return maxDistance
# @lc code=end

