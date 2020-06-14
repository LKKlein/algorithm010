/*
 * @lc app=leetcode.cn id=21 lang=golang
 *
 * [21] 合并两个有序链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	// 递归
	if l1 == nil {return l2}
	if l2 == nil {return l1}
	if l1.Val < l2.Val {
		l1.Next = mergeTwoLists(l1.Next, l2)
		return l1
	} else {
		l2.Next = mergeTwoLists(l1, l2.Next)
		return l2
	}
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	// 循环
	var head *ListNode = &ListNode{Val: 0}
	var cur *ListNode = head_node
	for l1 != nil && l2 != nil {
		if l1.Val > l2.Val {
			cur.Next = l2
			l2 = l2.Next
		} else {
			cur.Next = l1
			l1 = l1.Next
		}
		cur = cur.Next
	}

	if l1 == nil {
		cur.Next = l2
	} else {
		cur.Next = l1
	}
	return head.Next
}
// @lc code=end
