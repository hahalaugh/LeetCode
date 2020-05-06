import collections

class Solution(object):
    def threeSumHashLTE(self, nums):
        #纯哈希，LTE
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
        #排序，FIX第一个数后对候面进行2sum
        nums.sort()
        result = []
        
        def twoPointer(nums, target):
            i, j = 0, len(nums) - 1
            r = []
            while i < j:
                t = nums[i] + nums[j] 
                if t == target:
                    r.append([nums[i], nums[j]])
                    
                    #推进i,j到下一个不同的元素，防止重复
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
                #当被FIX的元素>0时，不需要继续往下进行，不可能得到等于0的组合了
                break
            if i > 0 and nums[i] == nums[i - 1]:
                #当前被FIX元素等于之前一个FIX元素时，跳过以防止重复结果
                continue
            
            step = twoPointer(nums[i + 1:], -nums[i])
            if step:
                for r in step:
                    result.append([nums[i]] + r)
        
        return result
    
    def threeSumCombination(self, nums):
        #排序 Combination 超时
        #排序 Combination+Hash勉强过
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
    
        
        