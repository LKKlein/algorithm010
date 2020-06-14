/*
 * @lc app=leetcode.cn id=88 lang=golang
 *
 * [88] 合并两个有序数组
 */

// @lc code=start
func merge(nums1 []int, m int, nums2 []int, n int)  {
	if m == 0 {
		copy(nums1, nums2)
	} else {
		var left, right int = 0, 0
		for right < n {
			if nums1[left] >= nums2[right] {
				copy(nums1[left + 1:m + right + 1], nums1[left:m + right])
				nums1[left] = nums2[right]
				right++
			}
			left++
			if left == m {
				copy(nums1[m + right:], nums2[right:])
			}
		}
	}
}
// @lc code=end

