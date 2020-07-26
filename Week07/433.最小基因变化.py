class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank: return -1
        from collections import defaultdict
        generate_bank = defaultdict(list)
        for gen in bank:
            for i in range(len(gen)):
                mask_word = gen[:i] + "_" + gen[i + 1:]
                generate_bank[mask_word].append(gen)
        return self.double_bfs(start, end, generate_bank)

    def double_bfs(self, start, end, generate_bank):
        start_queue, end_queue = [(start, 0)], [(end, 0)]
        start_visited, end_visited = {start: 0}, {end: 0}
        while start_queue or end_queue:
            if start_queue:
                ans = self.helper(start_queue, start_visited, end_visited, generate_bank)
                if ans: return ans

            if end_queue:
                ans = self.helper(end_queue, end_visited, start_visited, generate_bank)
                if ans: return ans
        return -1

    def helper(self, use_queue, use_visited, search_visited, bank):
        gen, level = use_queue.pop(0)
        if gen in search_visited:
            return level + search_visited[gen]
        
        for i in range(len(gen)):
            mask_word = gen[:i] + "_" + gen[i + 1:]
            for g in bank.get(mask_word, []):
                if g not in use_visited:
                    use_queue.append((g, level + 1))
                    use_visited[g] = level + 1
        return None
