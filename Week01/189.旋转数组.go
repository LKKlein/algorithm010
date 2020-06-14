/*
 * @lc app=leetcode.cn id=189 lang=golang
 *
 * [189] 旋转数组
 */

// @lc code=start
func rotate(nums []int, k int) {
	// 方法一：
	// 1. 双循环外层0~k，内层0~n，每个数分别移动k次
	// 时间复杂度为O(n*k)
	k = k % len(nums)
	for i := 0; i < k; i++ {
		start := 0
		for j := len(nums) - 1; j > 0; j -- {
			nums[j], nums[start] = nums[start], nums[j]
			start = j
		}
	}
}


func rotate2(nums []int, k int)  {
	// 方法二：
	// 1. 从第一个数开始，跟要到这个位置的数进行交换；
	// 2. 移动过去之后，再找到下一个要移动到当前这个位置的数进行交换；
	// 3. 重复2步骤，直到需要交换的数是第一个要交换的位置为止；
	// 4. 重复1，2，3步骤，直到数组内所有数字都被交换过；
	// 时间复杂度，由于每个数只会移动一次，所以为O(n)
	var n int = len(nums)
	k = k % n
	var start, end, count int = 0, 0, 0
	for count != n {
		end = start
		for {
			end = (end + k) % n
			if end == start {
				break
			}
			count++
			nums[end], nums[start] = nums[start], nums[end]
		}
		start++
		count++
	}
}


func rotate3(nums []int, k int)  {
	// 方法三：（有点难懂）
	// 1. 反转整个数组;
	// 2. 反转0~k-1的数；
	// 3. 反转k~n-1的数。
	// 时间复杂度，两次一半数组遍历，所以为O(n)
	k = k % len(nums)
	reverse(nums, 0, len(nums) - 1)
	reverse(nums, 0, k - 1)
	reverse(nums, k, len(nums) - 1)
}


func reverse(nums []int, start int, end int) {
	for start < end {
		nums[start], nums[end] = nums[end], nums[start]
		start++
		end--
	}
}
// @lc code=end

