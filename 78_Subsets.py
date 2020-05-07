class Solution(object):
    """
    生成子集的三种方法
Solution 1. 递归方式 - subset([1,2]) = subset(1) + (subset(1) x [2]) subset(1) = ([],[1]). subset(1) x [2] = ([],[1])x[2] = ([2],[1,2])
Solution 2. Backtracking. 长度0的全集 + 长度1的全部 ... + 长度为N的全部。
Solution 3. bitmask字典 [1,2,3] -> 1000 -> 1111 取下三位，000->111对应[1,2,3]中元素的出现或不出现。 最快
    """
    def subsets(self, nums):
        #字典序
        result = []
        n = len(nums)
        
        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            result.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return result
    
    def subsetsRecur(self, nums):
        #Non-Recursive Recursive
        result = [[]]
        for num in nums:
            result += [cur + [num] for cur in result]
        
        return result

    def subsetsBC(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #BC模板
        result = [[]]
        
        def bc(cur, idx, k):
            if len(cur) == k:
                result.append(cur[:])
            else:
                for i in range(idx, len(nums)):
                    cur.append(nums[i])
                    bc(cur, i+1, k)
                    cur.pop()
                    
        for k in range(1, len(nums)+1):
            bc([], 0, k)
        
        return result
    
        