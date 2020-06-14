/*
 * @lc app=leetcode.cn id=42 lang=golang
 *
 * [42] 接雨水
 */

// @lc code=start

// tag: 单调栈实现
func trap(height []int) int {
	var n, area int = len(height), 0
	if n <= 2 {
		return area
	}
	var stack []int = make([]int, n)
	var s_len int = 0
	for i := 0; i < n; i++ {
		// 如果当前元素大于单调栈的栈顶元素，就计算一下从栈顶元素到当前元素那一层的面积
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

// tag: 双指针实现
// 左右双指针，如果有一边的最大值比另一边最大值要低，说明低的那边肯定是能蓄水的，蓄水量等于低的这边的最大值减去当前的高度
func trap2(height []int) int {
	var n, area int = len(height), 0
	if n <= 2 {
		return area
	}
	var left, right int = 0, n - 1
	var l_max, r_max int = height[left], height[right]
	for left < right {
		if height[left] > l_max {
			l_max = height[left]
		}

		if height[right] > r_max {
			r_max = height[right]
		}

		if l_max <= r_max {
			area += l_max - height[left]
			left++
		} else {
			area += r_max - height[right]
			right--
		}
	}
	return area
}
// @lc code=end
