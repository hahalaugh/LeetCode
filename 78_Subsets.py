class Solution(object):
    """
    �����Ӽ������ַ���
Solution 1. �ݹ鷽ʽ - subset([1,2]) = subset(1) + (subset(1) x [2]) subset(1) = ([],[1]). subset(1) x [2] = ([],[1])x[2] = ([2],[1,2])
Solution 2. Backtracking. ����0��ȫ�� + ����1��ȫ�� ... + ����ΪN��ȫ����
Solution 3. bitmask�ֵ� [1,2,3] -> 1000 -> 1111 ȡ����λ��000->111��Ӧ[1,2,3]��Ԫ�صĳ��ֻ򲻳��֡� ���
    """
    def subsets(self, nums):
        #�ֵ���
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
        #BCģ��
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
    
        