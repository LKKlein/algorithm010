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

        return self.bfs({beginWord: 1}, {endWord: 0}, lookup)
    
    def bfs(self, beginWords, endWords, lookup, left_visited={}, right_visited={}):
        if len(beginWords) <= len(endWords):

            left_next_words = {}
            for beginWord, left_level in beginWords.items():
                if beginWord in endWords:
                    right_level = endWords[beginWord]
                    return left_level + right_level

                for i in range(len(beginWord)):
                    mask_word = beginWord[:i] + "*" + beginWord[i+1:]
                    for word in lookup.get(mask_word, []):
                        if word not in left_visited and word not in beginWords:
                            left_next_words[word] = left_level + 1
            if len(left_next_words) > 0:
                return self.bfs(left_next_words, endWords, lookup, dict(left_visited, **beginWords), right_visited)
            return 0

        else:

            right_next_words = {}
            for endWord, right_level in endWords.items():
                if endWord in beginWords:
                    left_level = beginWords[endWord]
                    return left_level + right_level

                for i in range(len(endWord)):
                    mask_word = endWord[:i] + "*" + endWord[i+1:]
                    for word in lookup.get(mask_word, []):
                        if word not in right_visited and word not in endWords:
                            right_next_words[word] = right_level + 1
            if len(right_next_words) > 0:
                return self.bfs(beginWords, right_next_words, lookup, left_visited, dict(right_visited, **endWords))
            return 0

# @lc code=end