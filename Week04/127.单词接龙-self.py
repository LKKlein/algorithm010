#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        lookup = {}
        for word in wordList:
            for i in range(len(word)):
                mask_word = word[:i] + "*" + word[i+1:]
                lookup[mask_word] = lookup.get(mask_word, []) + [word]

        return self.bfs([beginWord], endWord, lookup, 1)
    
    def bfs(self, beginWords, endWord, lookup, level, visited=[]):
        if endWord in beginWords:
            return level

        next_words = []
        for beginWord in beginWords:
            for i in range(len(beginWord)):
                mask_word = beginWord[:i] + "*" + beginWord[i+1:]
                for word in lookup.get(mask_word, []):
                    if word not in visited and word not in next_words and word not in beginWords:
                        next_words.append(word)

        if len(next_words) > 0:
            return self.bfs(next_words, endWord, lookup, level + 1, visited + beginWords)

        return 0
# @lc code=end