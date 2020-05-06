class Solution(object):
    #Solution 1. DFS, 永远只看第一个, 记录sum以避免重复计算
    #Solution 2. Backtracking 模式实现
    
    def combinationSum(self, candidates, target):
        result = []

        def dfs(candidates, target, idx, cur):
            if target < 0: 
                return 
            if target == 0 and cur: 
                result.append(cur)
                return 
            for i in range(idx, len(candidates)):
                cur.append(candidates[i])
                dfs(candidates, target-candidates[i], i, cur)
                cur.pop()
             
        return result
    
    def combinationSumDFS(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(nums, s, idx):
            if s > target:
                return
            elif nums and s == target:
                result.append(nums)
            elif idx < len(candidates):
                dfs(nums+[candidates[idx]], s+ candidates[idx], idx)
                dfs(nums, s, idx+1)
        
        dfs([], 0, 0)
        
        return result
