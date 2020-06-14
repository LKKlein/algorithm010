/*
 * @lc app=leetcode.cn id=66 lang=golang
 *
 * [66] 加一
 */

// @lc code=start
func plusOne(digits []int) []int {
	// 注意区分9和其他
	var remain int = 0
	var l int = len(digits)
	for i := l - 1; i >= 0; i -- {
		num := digits[i] + 1
		digits[i] = num % 10
		remain = num / 10
		if remain == 0 {
			return digits
		}
	}
	a := make([]int, l + 1)
	a[0] = remain
	copy(a[1:], digits)
	return a
}

// func plusOne(digits []int) []int {
// 	// 注意区分9和其他
// 	var l int = len(digits)
// 	for i := l - 1; i >= 0; i -- {
// 		if digits[i] == 9 {
// 			digits[i] += 1
// 			return digits
// 		} else {
// 			digits[i] = 0
// 		}
// 	}
// 	a := make([]int, l + 1)
// 	a[0] = 1
// 	copy(a[1:], digits)
// 	return a
// }
// @lc code=end

