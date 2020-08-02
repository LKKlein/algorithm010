# 学习笔记

## 位运算

### 十进制转二进制

将十进制数一直除以2的余数反向排列，就是二进制数。例如：

![156转为二进制](http://img.lkklein.xyz/Fh4NBHs0ra3T56fRXTdecva_0Yjh)

### 二进制转十进制

从右往左，从0开始，每一位的0、1代表该位置是否有2的指数，将所有指数计算完相加得到十进制。比如1000，表示第3位有2的指数，所以1000为8，而1010表示第1位和第3位有2的指数，则1010表示十进制的10。

### 位运算符

- 左移 <<

  二进制数字往左移动一位，右边用零填充。比如0011到0110

- 右移 >>

  二进制数字往右移动一位，左边用零填充。比如0011到0001

- 按位与 &

  参与运算的两个值，如果对应位都为1，则该位的结果为1，否则为0

- 按位或 | 

  只要对应位有一个为1时，结果位就为1

- 按位取反 ~

  对数据的每个二进制位取反，即把1变为0，把0变为1 。**~x** 类似于 **-x-1**

- 按位异或 ^

  当对应位不同时，结果为1

### N皇后问题（位运算求解）

```python3
class Solution:
    def totalNQueens(self, n):
        if n < 1: return [] 
        self.count = 0 
        self.DFS(n, 0, 0, 0, 0) 
        return self.count

    def DFS(self, n, row, cols, pie, na): 
        if row >= n:
            self.count += 1
            return

        bits = (~(cols | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits
            bits = bits & bits - 1
            self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
```



## LRU缓存（Python OrderedDict版本）

```python3
class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, /, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]
```



## 排序算法（待补充）

### 冒泡排序

```python3
def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```



### 快速排序

```python3
def quick_sort(arr):
    # 递归非原地排序
    if not arr:
        return []
    mid = arr.pop()
    left, right = [], []
    for item in arr:
        if item < mid:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left) + [mid] + quick_sort(right)


def quick_sort_v2(L):
    # 递归原地排序
    return q_sort(L, 0, len(L) - 1)


def q_sort(L, left, right):
    if left < right:
        pivot = partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L


def partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return left
```



### 归并排序

```python3
def merge(left, right):
    p, q = 0, 0
    arr = []
    while p < len(left) and q < len(right):
        if left[p] < right[q]:
            arr.append(left[p])
            p += 1
        elif left[p] >= right[q]:
            arr.append(right[q])
            q += 1
    if p == len(left):
        arr += right[q:]
    elif q == len(right):
        arr += left[p:]
    return arr


def merge_v2(left, right):
    arr = []
    while left and right:
        if left[0] < right[0]:
            arr.append(left.pop(0))
        else:
            arr.append(right.pop(0))
    if left:
        arr += left
    elif right:
        arr += right
    return arr


def merge_sort(arr):
    arr = [[n] for n in arr]
    while len(arr) > 1:
        left = arr.pop()
        right = arr.pop()
        sorted_arr = merge_v2(left, right)
        arr.insert(0, sorted_arr)
    return arr[0]


def recursive_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = recursive_merge_sort(left)
    right = recursive_merge_sort(right)
    return merge_v2(left, right)
```



### 堆排序

```python3
def heap_sort(arr):
    for start in range((len(arr) - 2) // 2, -1, -1):
        sift_down(arr, start, len(arr) - 1)

    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)
    return arr


def sift_down(arr, start, end):
    """最大堆调整"""
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break
```



