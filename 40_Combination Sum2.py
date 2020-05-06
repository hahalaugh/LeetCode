class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        def dfs(cur, idx, target):
            if target < 0: return
            if target == 0 and cur:
                result.append(tuple(cur[:]))
                return
            
            for i in range(idx, len(candidates)):
                cur.append(candidates[i])
                dfs(cur, i+1, target-cur[-1])
                cur.pop()
        
        dfs([], 0, target)
        return list(set(result))

s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
