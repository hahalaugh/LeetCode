class Solution(object):
    def combinationSum3(self, k, n):
        #生成所有长度为k的combination后，挑出其中和为n的combo
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [1,2,3,4,5,6,7,8,9]
        result = []
        
        def bc(cur, idx):
            if len(cur) == k and sum(cur) == n:
                result.append(cur[:])
            else:
                for i in range(idx, len(nums)):
                    cur.append(nums[i])
                    bc(cur, i+1)
                    cur.pop()
        
        bc([],0)
        
        #return [r for r in result if sum(r) == n]
        return result