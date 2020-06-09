class Solution(object):

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums: return False
        goal, rem = divmod(sum(nums), k)
        if rem > 0:
            return False

        def canPartition(group, nums):
            print(group, nums)
            if not nums: return True
            for i in range(len(group)):
                if group[i] + nums[-1] <= goal:
                    group[i] += nums[-1]
                    if canPartition(group, nums[:-1]):
                        return True
                    group[i] -= nums[-1]
                if group[i] == 0: break
            return False
        
        nums.sort()
        if nums[-1] > goal: return False
        while nums and nums[-1] == goal:
            nums.pop()
            k -= 1
        
        return canPartition([0] * k, nums)

                    
s = Solution()
print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
# print(s.canPartitionKSubsets([2, 2, 2, 2, 3, 4, 5], 4))
# print(s.canPartitionKSubsets([1, 1, 1, 1, 1], 5))
# print(s.canPartitionKSubsets([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 5))
