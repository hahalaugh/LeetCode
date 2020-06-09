class Solution(object):

    def rotate(self, nums, k):
        l = len(nums)
        count = l
        
        start = 0
        while count > 0:
            idx = start
            tmp = nums[idx]
            while True:
                idx = (idx + k) % l
                next = nums[idx]
                nums[idx] = tmp
                tmp = next
                count -= 1
                if idx == start:
                    break
            start += 1
        
    def rotateTrunkMove(self, nums, k):
        if not nums: return
        
        k %= len(nums)
        idx = len(nums) - k
        tmp = nums[idx:]
        nums[k:] = nums[:idx]
        nums[:k] = tmp

    def rotatePopInsert(self, nums, k):
        # pop + insert
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        
        k %= len(nums)
        
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
        
    
s = Solution()
a = [1, 2, 3, 4, 5, 6, 7]
s.rotate(a, 3)
print(a)
