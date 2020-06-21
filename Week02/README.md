# 学习笔记

## 二叉树的遍历

1. 前序遍历(Pre-order)：根-左-右 
2. 中序遍历(In-order)：左-根-右
3. 后序遍历(Post-order)：左-右-根
4. 层序遍历：Z字形遍历（BFS）

代码实现：

```python3
class TreeNode():
    """ 定义一棵二叉树 """

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree():

    def __init__(self):
        self.data = []  # 遍历结果

    # ===============  递归遍历  =================
    # 1. 递归遍历思路清晰，只需调换不同遍历类型的顺序

    def preorder(self, root):
        # 前序遍历：根->左->右
        if root:
            self.data.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        # 中序遍历：左->根->右
        if root:
            self.inorder(root.left)
            self.data.append(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        # 后序遍历：右->左->根
        if root:
            self.postorder(root.right)
            self.postorder(root.left)
            self.data.append(root.val)

    def levelorder(self, root):
        # 层序遍历
        if root and not isinstance(root, list):
            root = [root]
        if root:
            children = []
            vals = []
            for node in root:
                vals.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            if vals:
                self.data.append(vals)
            self.levelorder(children)

    # ==============  非递归，循环遍历 ===============
    # 1. 使用栈手动维护，类似于递归
    # 2. 栈后进先出，因此入栈顺序与递归顺序相反
    #    前序入栈：右左根
    #    中序入栈：右根左
    #    后续入栈：根左右

    def preorder_v2(self, root):
        stack = [root]
        while stack:
            d = stack.pop()
            if isinstance(d, TreeNode):
                stack.extend([d.right, d.left, d.val])
            elif isinstance(d, int):  # val的实际类型
                self.data.append(d)

    def inorder_v2(self, root):
        stack = [root]
        while stack:
            d = stack.pop()
            if isinstance(d, TreeNode):
                stack.extend([d.right, d.val, d.left])
            elif isinstance(d, int):
                self.data.append(d)

    def postorder_v2(self, root):
        stack = [root]
        while stack:
            d = stack.pop()
            if isinstance(d, TreeNode):
                stack.extend([d.val, d.left, d.right])
            elif isinstance(d, int):
                self.data.append(d)

    def levelorder_v2(self, root):
        if root:
            queue = [root]
            while len(queue) != 0:
                res = []
                n = len(queue)
                for i in range(n):
                    node = queue.pop(0)
                    res.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                self.data.append(res)

```



## 二叉搜索树

一颗空树或者具有以下特点：

1. 左子树上所有结点的值均小于它的根结点的值
2. 右子树上所有结点的值均大于它的根结点的值
3. 以此类推：左、右子树也分别为二叉查找树。 

中序遍历树：升序



## 二叉堆

1. 满足以下特性：
   - 是一颗**完全二叉树**
   - 树中任意节点的值都是大于等于其子节点的值
2. 二叉堆一般使用“数组”实现
3. 假设根节点的索引为0，那么堆中父节点与子节点的关系如下：
   - 索引为`i`的左孩子的索引是`2 * i + 1`
   - 索引为`i`的右孩子的索引是`2 * i + 2`
   - 索引为`i`的父节点的索引是`floor((i - 1) / 2) `
4. Insert插入操作HeapifyUp
   - 先插入到数组尾部
   - 然后依次与父节点比较，不断向上调整，直到满足条件
5. Delete删除操作HeapifyDown
   - 直接删除当前元素，并将数组尾部元素替换到当前位置
   - 然后将其与子节点比较，不断与较大的子节点交换，向下调整，直到尾部



## 图

- 广度优先搜索（BFS）

```python3
def bfs(root):
		queue = [root]
		visited = []   # 图遍历必写，防止访问重复点
		while queue:
				node = queue.pop(0)
				visited.append(node)
				# 相关处理
				process(node)
				# 获取相邻的节点
				nodes = generate_relate_nodes(node)
				for n in nodes:
						queue.append(n)
```



- 深度优先搜索（DFS）

```python3
visited = set()
def dfs(node, visited):
		if node in visited:
				return
				
		visited.add(node)
		# 相关处理
		process(node)
		for next_node in node.children():
				if next_node not in visited:
						dfs(next_node, visited)
```



## 排序（时间O(nlogn)总结）

### 快速排序 quick_sort

- 递归非原地排序版本（时间O(nlogn)，空间O(n)）

```python3
def quick_sort(arr):
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
```

- 递归原地排序版本（时间O(nlogn)，空间O(1)）

```python3
def quick_sort_v2(arr):
    q_sort(arr, 0, len(L) - 1)
    return arr


def q_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)

        q_sort(arr, left, pivot - 1)
        q_sort(L, pivot + 1, right)


def partition(arr, left, right):
    pivotkey = arr[left]

    while left < right:
        while left < right and arr[right] >= pivotkey:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivotkey:
            left += 1
        arr[right] = arr[left]

    arr[left] = pivotkey
    return left
```

### 归并排序 merge_sort

时间O(nlogn)，空间O(n)

- 循环版本

```python3
def merge(left, right):
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
```

- 递归版本

```python3
def recursive_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = recursive_merge_sort(left)
    right = recursive_merge_sort(right)
    return merge(left, right)
```

### 堆排序 heap_sort

详细讲解见[该文](https://www.cnblogs.com/chengxiao/p/6129630.html)

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

