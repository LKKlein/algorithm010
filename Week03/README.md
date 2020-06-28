# 学习笔记

## 递归

#### 代码模板

1. 递归终止条件
2. 处理当前层逻辑
3. 下探到下一层
4. 清理当前层变量环境等

```python3
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
       process_result 
       return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```

#### 思维要点

1. 抵制人肉递归
2. 找最近重复性
3. 数学归纳法思维



## 分治

### 代码模板

```python3
def divide_conquer(problem, param1, param2, ...): 
    # recursion terminator 
    if problem is None: 
    print_result 
    return 
    # prepare data 
    data = prepare_data(problem) 
    subproblems = split_problem(problem, data) 
    # conquer subproblems 
    subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
    subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
    subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
    …
    # process and generate the final result 
    result = process_result(subresult1, subresult2, subresult3, …)

    # revert the current level states
```


