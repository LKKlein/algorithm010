class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 0: return 0
        # 任务列表转词典并排序任务量
        from collections import defaultdict
        task_center = defaultdict(int)
        for task in tasks:
            task_center[task] += 1
        task_list = list(sorted(task_center.values(), reverse=True))
        m = len(task_list)

        # 任务量最多的为基时间数
        max_tasks = task_list.pop(0)
        ans = (n + 1) * (max_tasks - 1) + 1

        # 后续如果任务数量相同, 则总数 + 1， 否则就填充到待命区域
        while n > 0 and len(task_list) > 0 and task_list.pop(0) == max_tasks:
            ans += 1
            n -= 1

        # 如果待命区域用完，那就是所有任务都可以直接交替完成，那就是任务长度
        return max(ans, len(tasks))
