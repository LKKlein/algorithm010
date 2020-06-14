/*
 * @lc app=leetcode.cn id=283 lang=golang
 *
 * [283] 移动零
 */

// @lc code=start
func moveZeroes(nums []int)  {
	lens := len(nums)
	start, n := 0, 0
	for n < lens {
		if nums[n] != 0 {
			nums[n], nums[start] = nums[start], nums[n]
			start++
		}
		n++
	}
}
// @lc code=end

