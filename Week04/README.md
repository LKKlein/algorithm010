# 学习笔记

## 深度优先搜索 DFS (栈 or 递归)

- 递归版本

```python3
visited = set() 
def dfs(node, visited):
    if node in visited: # terminator
        # already visited 
        return 
    visited.add(node) 
    # process current node here. 
    ...
    for next_node in node.children(): 
        if next_node not in visited: 
            dfs(next_node, visited)
```

- 非递归版本

```python3
def DFS(self, tree): 
    if tree.root is None: 
        return [] 
    visited, stack = [], [tree.root]
    while stack: 
        node = stack.pop() 
        visited.add(node)
        process (node) 
        nodes = generate_related_nodes(node) 
        stack.push(nodes) 
    # other processing work 
    ...
```



## 广度优先搜索BFS （队列 or 递归）

- 队列版本

```python3
def BFS(graph, start, end):
    visited = set()
    queue = [] 
    queue.append([start]) 
    while queue: 
        node = queue.pop() 
        visited.add(node)
        process(node) 
        nodes = generate_related_nodes(node) 
        queue.push(nodes)
    # other processing work 
    ...
```

- 递归版本

```python3
visited = set() 
def BFS(nodes, visited):
    next_nodes = []
    for node in nodes:
        if node in visited:
            continue
        visited.add(node)
        # process current node here. 
        for child in node.children():
            next_nodes.append(child)
    self.BFS(next_nodes, visited) 
```



## 贪心算法

- 贪心算法：选择当前局部最优解，且不能回溯
- 动态规划：探索所有可能并保存以前的结果，得到全局最优，可以回退

一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。

简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构。



## 二分查找

- 代码模板

```python3
def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) / 2
        if array[mid] == target: # find the target!! 
            break or return result 
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
```



