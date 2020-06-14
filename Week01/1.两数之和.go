/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i, v := range nums {
		real_target := target - v
		ele, exist := m[real_target]
		m[v] = i
		if exist {
			return []int{ele, i}
		}
	}
	return []int{}
}
// @lc code=end

