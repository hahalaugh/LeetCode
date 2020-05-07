class Solution(object):
    def subsetsWithDup(self, nums):
        #���� + BC��i == i-1 ȥ��
        nums.sort()
        result = []
        def bc(cur, idx, k):
            if len(cur) == k:
                result.append(cur[:])
            else:
                for i in range(idx, len(nums)):
                    if i > idx and nums[i] == nums[i-1]:
                        continue
                    cur.append(nums[i])
                    bc(cur, i+1, k)
                    cur.pop()
        
        for k in range(len(nums)+1):
            bc([],0,k)
        
        return result
    
    def subsetsWithDupSetSort(self, nums):
        #�ݹ�����set+sortȥ�أ���Ȼͨ��
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        s = set()
        for num in nums:
            result += [cur + [num] for cur in result]
        
        for r in result:
            s.add(tuple(sorted(r)))
        
        return s
        

s = Solution()
print(s.subsetsWithDup([1,2,2]))