/*
 * @lc app=leetcode.cn id=127 lang=golang
 *
 * [127] 单词接龙
 */

// @lc code=start
func ladderLength(beginWord string, endWord string, wordList []string) int {
    if !ContainsInArray(wordList, endWord) {
		return 0
	}

	lookup := Construct_words(wordList)
	visited := make([]string, 10)
	return BFSWord([]string{beginWord}, endWord, 1, lookup, visited)
}

func Construct_words(wordList []string) (lookup map[string][]string) {
	lookup = make(map[string][]string)
	for _, word := range wordList {
		for i := 0; i < len(word); i++ {
			mask_word := word[:i] + "*" + word[i+1:]
			_, ok := lookup[mask_word]
			if !ok {
				lookup[mask_word] = make([]string, 1)
			}
			lookup[mask_word] = append(lookup[mask_word], word)
		}
	}
	return
}

func BFSWord(beginWords []string, endWord string, level int, lookup map[string][]string, visited []string) int {
	if ContainsInArray(beginWords, endWord) {
		return level
	}

	next_words := make([]string, 0)
	for _, beginWord := range beginWords {
		for i := 0; i < len(beginWord); i++ {
			mask_word := beginWord[:i] + "*" + beginWord[i+1:]
			found_words, ok := lookup[mask_word]
			if ok {
				for _, word := range found_words {
					if !ContainsInArray(visited, word) && !ContainsInArray(beginWords, word) && !ContainsInArray(next_words, word) {
						next_words = append(next_words, word)
					}
				}
			}
		}
	}

	if len(next_words) != 0 {
		return BFSWord(next_words, endWord, level + 1, lookup, append(visited, beginWords...))
	}

	return 0
}

func ContainsInArray(wordList []string, key string) bool {
	for _, word := range wordList {
		if key == word {
			return true
		}
	}
	return false
}
// @lc code=end

