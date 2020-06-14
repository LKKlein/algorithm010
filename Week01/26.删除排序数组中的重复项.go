/*
 * @lc app=leetcode.cn id=26 lang=golang
 *
 * [26] 删除排序数组中的重复项
 */

// @lc code=start
func removeDuplicates(nums []int) int {
	total := len(nums) - 1
	if total <= 0 {
		return total + 1
	}
	start := 0
	for i := 0; i <= total - 1; i ++ {
		if nums[i] != nums[i + 1] {
			nums[start], nums[i] = nums[i], nums[start]
			start += 1
		}
	}
	nums[start], nums[total] = nums[total], nums[start]
	return start + 1
}
// @lc code=end

