class Solution(object):
    #Solution 1. DFS, 永远只看第一个, 记录sum以避免重复计算
    #Solution 2. Backtracking 模式实现
    
    def combinationSum(self, candidates, target):
        result = []
        
        def bc(r, candidates):
            if not candidates: return 
            
            for i in range(len(candidates)):
                if sum(r) <= target - candidates[i]:
                    r = r + [candidates[i]]
                    if sum(r) == target:
                        result.append(r)
                    else:
                        bc(r,candidates[i:])
                    r = r[:-1]
        
        bc([], candidates)
        
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