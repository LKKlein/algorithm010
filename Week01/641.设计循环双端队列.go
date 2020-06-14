/*
 * @lc app=leetcode.cn id=641 lang=golang
 *
 * [641] 设计循环双端队列
 */

// @lc code=start
import "fmt"

type MyCircularDeque struct {
	data []int
	head int
	tail int
	size int
	capacity int
}


/** Initialize your data structure here. Set the size of the deque to be k. */
func Constructor(k int) MyCircularDeque {
	return MyCircularDeque{
		data: make([]int, k + 1),
		head: 0,
		tail: 0,
		size: k + 1,
		capacity: k,
	}
}


/** Adds an item at the front of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) InsertFront(value int) bool {
	if this.IsFull() {
		return false
	}
	fmt.Println("head", this.head, this.tail, this.data)
	this.head = (this.head + this.size - 1) % this.size
	this.data[this.head] = value
	return true
}


/** Adds an item at the rear of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) InsertLast(value int) bool {
	if this.IsFull() {
		return false
	}
	fmt.Println("tail", this.head, this.tail, this.data)
	this.tail = (this.tail + 1) % this.size
	this.data[this.tail] = value
	return true
}


/** Deletes an item from the front of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) DeleteFront() bool {
	if this.IsEmpty() {
		return false
	}
	fmt.Println("d-h", this.head, this.tail, this.data)
	this.head = (this.head + 1) % this.size
	return true
}


/** Deletes an item from the rear of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) DeleteLast() bool {
	if this.IsEmpty() {
		return false
	}
	fmt.Println("d-l", this.head, this.tail, this.data)
	this.tail = (this.tail + this.size - 1) % this.size
	return true
}


/** Get the front item from the deque. */
func (this *MyCircularDeque) GetFront() int {
	if this.IsEmpty() {
		return -1
	}
	fmt.Println("g-h", this.head, this.tail, this.data)
	return this.data[this.head]
}


/** Get the last item from the deque. */
func (this *MyCircularDeque) GetRear() int {
	if this.IsEmpty() {
		return -1
	}
	fmt.Println("g-l", this.head, this.tail, this.data)
	return this.data[this.tail]
}


/** Checks whether the circular deque is empty or not. */
func (this *MyCircularDeque) IsEmpty() bool {
	return this.head == this.tail
}


/** Checks whether the circular deque is full or not. */
func (this *MyCircularDeque) IsFull() bool {
	return this.head == (this.tail + 1) % this.size
}


/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.InsertFront(value);
 * param_2 := obj.InsertLast(value);
 * param_3 := obj.DeleteFront();
 * param_4 := obj.DeleteLast();
 * param_5 := obj.GetFront();
 * param_6 := obj.GetRear();
 * param_7 := obj.IsEmpty();
 * param_8 := obj.IsFull();
 */
// @lc code=end

// ["MyCircularDeque","insertFront","getRear","insertFront","getRear","insertLast","getFront","getRear","getFront","insertLast","deleteLast","getFront"]\n[[3],[9],[],[9],[],[5],[],[],[],[8],[],[]]