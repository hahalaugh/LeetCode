class Solution(object):

    def findDuplicate(self, nums):
        # Circle Detection
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        
    def findDuplicateBinarySearch(self, nums):
        i, j = 1, len(nums) - 1
        while i < j:
            m = i + (j - i) / 2
            count = sum(1 for n in nums if n <= m)
            if count > m:
                j = m
            else:
                i = m + 1
        return i
    
    def findDuplicateSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
    
    def findDuplicateSet(self, nums):
        s = set()
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                return n
    
    def findDuplicateBruteForce(self, nums):
        for i in range(len(nums)):
            for j in range(len(i + 1, len(nums))):
                if nums[i] == nums[j]:
                    return nums[i]
        
        
