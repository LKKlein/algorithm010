class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        from collections import defaultdict
        word_tables = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                mask_word = word[:i] + "_" + word[i + 1:]
                word_tables[mask_word].append(word)

        return self.double_bfs(beginWord, endWord, word_tables)
        
    def double_bfs(self, beginWord, endWord, word_tables):
        begin_queue, end_queue = [(beginWord, 0)], [(endWord, 1)]
        begin_visited, end_visited = {beginWord: 0}, {endWord: 1}
        while begin_queue or end_queue:
            if begin_queue:
                word, level = begin_queue.pop(0)
                if word in end_visited:
                    return level + end_visited[word]
                
                for i in range(len(word)):
                    mask_word = word[:i] + "_" + word[i + 1:]
                    for w in word_tables[mask_word]:
                        if w not in begin_visited:
                            begin_queue.append((w, level + 1))
                            begin_visited[w] = level + 1
            
            if end_queue:
                word, level = end_queue.pop(0)
                if word in begin_visited:
                    return level + begin_visited[word]
                
                for i in range(len(word)):
                    mask_word = word[:i] + "_" + word[i + 1:]
                    for w in word_tables[mask_word]:
                        if w not in end_visited:
                            end_queue.append((w, level + 1))
                            end_visited[w] = level + 1
        return 0
