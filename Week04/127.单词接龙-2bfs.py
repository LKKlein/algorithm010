#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        lookup = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                mask_word = word[:i] + "*" + word[i+1:]
                lookup[mask_word].append(word)

        return self.bfs([beginWord], [endWord], lookup, 1, 0)
    
    def bfs(self, beginWords, endWords, lookup, left_level, right_level, left_visited=[], right_visited=[]):
        if len(beginWords) <= len(endWords):

            left_next_words = []
            for beginWord in beginWords:
                if beginWord in endWords:
                    return left_level + right_level

                for i in range(len(beginWord)):
                    mask_word = beginWord[:i] + "*" + beginWord[i+1:]
                    for word in lookup.get(mask_word, []):
                        if word not in left_visited and word not in left_next_words and word not in beginWords:
                            left_next_words.append(word)
            if len(left_next_words) > 0:
                return self.bfs(left_next_words, endWords, lookup, left_level + 1,
                                right_level, left_visited + beginWords, right_visited)
            return 0

        else:

            right_next_words = []
            for endWord in endWords:
                if endWord in beginWords:
                    return left_level + right_level

                for i in range(len(endWord)):
                    mask_word = endWord[:i] + "*" + endWord[i+1:]
                    for word in lookup.get(mask_word, []):
                        if word not in right_visited and word not in right_next_words and word not in endWords:
                            right_next_words.append(word)
            if len(right_next_words) > 0:
                return self.bfs(beginWords, right_next_words, lookup, left_level,
                                right_level + 1, left_visited, right_visited + endWords)
            return 0

# @lc code=end