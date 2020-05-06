import collections

class Solution(object):
    def threeSumHashLTE(self, nums):
        #����ϣ��LTE
        if not nums: return []
        
        result = set()
        
        d = collections.defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)-1):
                target = -nums[i]-nums[j]
                if target in d and max(d[target]) > j:
                    result.add(tuple(sorted((nums[i], nums[j], target))))
        return result
    
    def threeSum(self, nums):
        #����FIX��һ������Ժ������2sum
        nums.sort()
        result = []
        
        def twoPointer(nums, target):
            i, j = 0, len(nums) - 1
            r = []
            while i < j:
                t = nums[i] + nums[j] 
                if t == target:
                    r.append([nums[i], nums[j]])
                    
                    #�ƽ�i,j����һ����ͬ��Ԫ�أ���ֹ�ظ�
                    while i < len(nums) - 1: 
                        i += 1
                        if nums[i - 1] != nums[i]: break
                        
                    while j > 0:
                        j -= 1
                        if nums[j + 1] != nums[j]: break
                    
                elif t > target:
                    j -= 1
                else:
                    i += 1
            return r
        
        for i in range(0, len(nums) - 1):
            if nums[i] > 0: 
                #����FIX��Ԫ��>0ʱ������Ҫ�������½��У������ܵõ�����0�������
                break
            if i > 0 and nums[i] == nums[i - 1]:
                #��ǰ��FIXԪ�ص���֮ǰһ��FIXԪ��ʱ�������Է�ֹ�ظ����
                continue
            
            step = twoPointer(nums[i + 1:], -nums[i])
            if step:
                for r in step:
                    result.append([nums[i]] + r)
        
        return result
    
    def threeSumCombination(self, nums):
        #���� Combination ��ʱ
        #���� Combination+Hash��ǿ��
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        d = collections.defaultdict(list)
        
        for i in range(len(nums)):
            d[nums[i]].append(i)
        
        #print(nums)
        def contains(d, target, idx):
            if target not in d: return False
            return max(d[target]) >= idx
        
        def dfs(r, idx, target):
            if len(r) == 2:
                #if target in nums[idx:]:
                if contains(d, target, idx):
                    result.append(r+[target])
                else:
                    return
            else:
                for i in range(idx, len(nums)):
                    if i > idx and nums[i] == nums[i-1]:
                        continue
                    r.append(nums[i])
                    dfs(r, i+1, target-nums[i])
                    r.pop()
        
        dfs([], 0, 0)
        return result
    
        
        