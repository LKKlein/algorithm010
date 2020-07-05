#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        lookup = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                mask_word = word[:i] + "*" + word[i+1:]
                lookup[mask_word].append(word)

        return self.bfs(beginWord, endWord, lookup)
    
    def bfs(self, beginWord, endWord, lookup):
        queue, visited = deque([(beginWord, 1)]), {beginWord: 1}
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                mask = word[:i] + "*" + word[i+1:]
                for neigh in lookup.get(mask, []):
                    if neigh not in visited:
                        visited[neigh] = steps + 1
                        queue.append((neigh, steps + 1))
        return 0

    # def bfs(self, beginWord, endWord, lookup):
    #     left_queue, right_queue = deque([(beginWord, 1)]), deque([(endWord, 0)])
    #     left_visited = {beginWord: 1}
    #     right_visited = {endWord: 0}
    #     while left_queue and right_queue:
    #         ans = self.visitNode(lookup, left_queue, left_visited, right_visited)
    #         if ans: return ans
    #         ans = self.visitNode(lookup, right_queue, right_visited, left_visited)
    #         if ans: return ans
    #     return 0

    # def visitNode(self, lookup, queue, visited, other_visited):
    #     word, steps = queue.popleft()
    #     for i in range(len(word)):
    #         mask = word[:i] + "*" + word[i+1:]
    #         for neigh in lookup.get(mask, []):
    #             if neigh in other_visited:
    #                 return steps + 1 + other_visited[neigh]
    #             if neigh not in visited:
    #                 visited[neigh] = steps + 1
    #                 queue.append((neigh, steps + 1)) 
    #     return None
# @lc code=end

