import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        h = []
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
            else:
                small = heapq.nsmallest(1, h)
                if n > h[0]:
                    heapq.heappushpop(h, n)
        
        return heapq.heappop(h)

    def findKthLargestQuickSort(self, nums, k):
        def partition(i, j):
            l, r = i-1, i
            pivot = nums[j]
            while r < j:
                if nums[r] < pivot:
                    l += 1
                    nums[l], nums[r] = nums[r], nums[l]
                r += 1
            nums[l+1], nums[j] = nums[j], nums[l+1]
            return l+1
        
        i,j = 0, len(nums)-1
        
        while True:
            idx = partition(i, j)
            if idx == len(nums)-k:
                return nums[idx]
            elif idx > len(nums)-k:
                j = idx - 1
            else:
                i = idx + 1
        
        
    def findKthLargestSort(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)-k]
s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))