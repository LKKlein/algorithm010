/*
 * @lc app=leetcode.cn id=42 lang=golang
 *
 * [42] 接雨水
 */

// @lc code=start
func trap(height []int) int {
	// 单调栈实现
	var n, area int = len(height), 0
	if n <= 2 {
		return area
	}
	var stack []int = make([]int, n)
	var s_len int = 0
	for i := 0; i < n; i++ {
		for s_len > 0 && height[i] >= height[stack[s_len - 1]] {
			delta_h := min(height[i], height[stack[s_len - 1]]) - height[stack[s_len]]
			w := i - stack[s_len - 1] - 1
			area += w * delta_h
			s_len--
		}
		// 多计算一次，避免漏掉当前元素比栈顶元素低，比前一个栈顶元素高的情况[3,1,2]
		if s_len > 0 && height[i] < height[stack[s_len - 1]] {
			delta_h := min(height[i], height[stack[s_len - 1]]) - height[stack[s_len]]
			w := i - stack[s_len - 1] - 1
			area += w * delta_h
		}
		stack[s_len] = i
		s_len++
	}
	return area
}

func min(a int, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}
// @lc code=end

