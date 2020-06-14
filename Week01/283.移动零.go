/*
 * @lc app=leetcode.cn id=283 lang=golang
 *
 * [283] 移动零
 */

// @lc code=start

// 滚雪球大法：遇到非零元素，就将该元素与0000的第一个交换
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

